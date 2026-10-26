"""Read evidence for project-plan progress without changing project documents (WAY-153).

Usage: python -B <the-way>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY

Exit codes: 0 for a completed observation (unchecked evidence can remain), 1 for source
findings or conflicting task states, 2 for invocation, source-read or Git operational errors.
Only Git metadata is refreshed; proposals never apply changes to the plan or task documents.
Command output is UTF-8, including redirected reports and diagnostics.
"""

import argparse
import os
from pathlib import Path
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote
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
    """Inventory ordinary blobs without following symlinks or imposing record basenames."""
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


def record_pointers(git, commit, paths):
    """Read pointer text as data, without executing or printing the archive's instructions."""
    result = git.run("grep", "-I", "-z", "-n", "-E",
                     r"https?://[^ ]+/(pull|merge_requests)/[0-9]+", commit, "--",
                     *(":(literal)" + path for path in paths), allowed=(0, 1))
    pointers = []
    for row in result.stdout.splitlines():
        parts = row.split(b"\0", 2)
        if len(parts) == 3:
            source = parts[0].decode("utf-8")
            for link in PR_LINK.findall(parts[2].decode("utf-8", errors="replace")):
                pointers.append((source, link))
    return sorted(set(pointers))


def path_value(value):
    """Read a literal path or a whole Markdown path link; never interpret it as a command."""
    value = value.strip()
    link = re.fullmatch(r"\[[^\]\n]*\]\((.+)\)", value)
    if link:
        value = link[1]
    return value.strip("`<>")


def source_path(value, parent=None):
    value = path_value(value)
    if not value or any(char in value for char in "\r\n\0") or "://" in value:
        return None
    path = Path(value)
    if not path.is_absolute():
        if parent is None:
            return None
        path = parent / path
    # Lexical normalization keeps missing/moved sources unresolved rather than searching by name.
    return os.path.normcase(os.path.abspath(path))


def leading_values(value):
    """Yield the whole value and each prefix ending where a record annotation may begin."""
    # Cycles write a path followed by free annotations; separators can also occur inside a path,
    # so every cut is a candidate and none is chosen before comparing with a known identity.
    for separator in re.finditer(r"; |, | — | \(|`", value):
        yield value[:separator.start()]
    yield value


def frozen_link(document):
    """Read a Document link to a task's frozen copy as a product commit and path, or None."""
    link = re.fullmatch(r"https?://[^/\s]+/\S*?/(?:-/)?blob/([0-9a-f]{7,40})/([^?#\s]+)(?:[?#]\S*)?",
                        path_value(document))
    if not link or any(not char.isprintable() for char in unquote(link[2])):
        return None
    return link[1], unquote(link[2])


def bare_name(value):
    name = path_value(value)
    return "/" not in name and "\\" not in name


def names_plan(value, parents, plan_path):
    """Accept a plan path relative to a task document's folder or the plan's bare file name."""
    if bare_name(value) and os.path.normcase(path_value(value)) == \
            os.path.normcase(os.path.basename(plan_path)):
        return True
    return any(source_path(value, parent) == source_path(plan_path) for parent in parents)


def unsure(value, frozen_copy):
    """A relative plan path cannot be refuted once only a frozen copy anchors the task."""
    return frozen_copy is not None and not bare_name(value)


def header_fields(text, label):
    fields = []
    for line in text.splitlines():
        if line.startswith(("## ", "```", "~~~")):
            break
        match = re.fullmatch(r"(?:- )?" + re.escape(label) + r": (.+)", line)
        if match:
            fields.append(match[1])
    return fields


def provenance(paths, read, plan_path, task, frozen_copy=None):
    """Associate each record with its own retained task, anchored at its original source.

    A Document linking the task's frozen copy anchors records by that copy's text instead
    (frozen_copy); False marks a linked copy the product repository cannot supply.
    """
    document = source_path(task.document, Path(plan_path).parent)
    owned, unresolved, foreign = [], [], []
    for path in paths:
        text = read(path)
        sources = header_fields(text, "Task source")
        relations = header_fields(text, "Task relation")
        if not sources and not relations:
            continue
        if len(sources) != 1 or len(relations) != 1:
            unresolved.append(path + ": missing or ambiguous task provenance fields")
            continue
        if frozen_copy is False:
            unresolved.append(path + ": frozen copy the Document links is absent from the product "
                              "repository")
            continue
        candidates = [candidate for candidate in map(source_path, leading_values(sources[0]))
                      if candidate is not None]
        if frozen_copy is None:
            if not candidates or document is None or task.document == "—":
                unresolved.append(path + ": original Task source or Document cannot be anchored")
                continue
            if document not in candidates:
                foreign.append(path + ": Task source " + sources[0] + " differs from Document " +
                               document)
                continue
            parents = [Path(document).parent]
        else:
            # The source document is gone; any folder its recorded path may name can hold it.
            parents = [Path(candidate).parent for candidate in candidates]
        if not re.match(r"plan item(?![\w-])", relations[0]):
            unresolved.append(path + ": same-source Task relation does not establish this plan's membership")
            continue
        # The frozen task binds plan and name below; only the one expanded form also names them.
        relation = re.fullmatch(r"plan item — (.+?) \([^\n]+\), item ([1-9][0-9]*) "
                                r"([a-z0-9]+(?:-[a-z0-9]+)*)(?:; .+)?", relations[0])
        if relation:
            related_plan = source_path(relation[1], parents[0]) if parents else relation[1]
            if not names_plan(relation[1], parents, plan_path) or relation[3] != task.name:
                if unsure(relation[1], frozen_copy) and relation[3] == task.name:
                    unresolved.append(path + ": Task relation's plan cannot be resolved without "
                                      "the removed source document")
                    continue
                foreign.append(path + ": Task relation names plan " + str(related_plan) +
                               " item " + relation[2] + " " + relation[3])
                continue
        artifacts = re.search(r"^## Artifacts\s*\n(.*?)(?=^## |\Z)", text,
                              re.MULTILINE | re.DOTALL)
        frozen = []
        if artifacts:
            for line in artifacts[1].splitlines():
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) >= 2 and cells[0].lower() == "frozen task":
                    frozen.append(cells[1])
        if len(frozen) != 1:
            unresolved.append(path + ": missing or ambiguous frozen task artifact")
            continue
        # Frozen artifacts must belong to this snapshot, not today's external source or another cycle.
        targets = {posixpath.normpath(posixpath.join(posixpath.dirname(path),
                                                     path_value(value).replace("\\", "/")))
                   for value in leading_values(frozen[0]) if path_value(value)} & set(paths)
        if len(targets) != 1:
            unresolved.append(path + ": frozen task artifact absent from this cycle snapshot")
            continue
        target = targets.pop()
        if frozen_copy is not None and \
                read(target).replace("\r\n", "\n") != frozen_copy.replace("\r\n", "\n"):
            foreign.append(path + ": frozen task differs from the frozen copy the Document links")
            continue
        memberships = header_fields(read(target), "Project relation")
        if len(memberships) != 1:
            unresolved.append(path + ": missing or ambiguous frozen task membership")
            continue
        membership = re.fullmatch(r"plan item: (.+) — ([a-z0-9]+(?:-[a-z0-9]+)*)",
                                  memberships[0])
        if not membership:
            unresolved.append(path + ": frozen task membership cannot be read")
            continue
        member_plan = source_path(membership[1], parents[0]) if parents else membership[1]
        if not names_plan(membership[1], parents, plan_path) or membership[2] != task.name:
            if unsure(membership[1], frozen_copy) and membership[2] == task.name:
                unresolved.append(path + ": frozen task's plan cannot be resolved without the "
                                  "removed source document")
                continue
            foreign.append(path + ": frozen task names plan " + str(member_plan) +
                           " task " + membership[2] + ", not the supplied plan/task")
            continue
        owned.append(path)
    if foreign:
        return "foreign", owned, foreign
    if unresolved:
        return "unchecked", [], unresolved
    if not owned:
        return "unchecked", [], ["missing recorded task provenance in cycle snapshot"]
    return "owned", owned, []


def task_report(git, observation, task, plan_path):
    prefix = "%d %s" % (task.number, task.name)
    lines = ["task %s: %s" % (prefix, task.state)]
    active, archived, merged = [], [], []
    unchecked, errors, contradictions = [], [], []
    working = ".runs/task-cycles/" + task.name
    archive = "docs/task-cycles/" + task.name + "/"
    try:
        frozen_copy, link = None, frozen_link(task.document)
        if link:
            blob = git.run("cat-file", "blob", "%s:%s" % link, allowed=(0, 128))
            frozen_copy = not blob.returncode and blob.stdout.decode("utf-8", errors="replace")
        for worktree in observation.worktrees:
            path = worktree / working
            try:
                if path.is_dir():
                    files = [file for file in path.rglob("*") if file.is_file() and
                             not any(parent.is_symlink() for parent in (file, *file.parents))]
                    paths = [file.relative_to(path).as_posix() for file in files]
                    status, _, reasons = provenance(paths, lambda name: (path / name).read_text(
                        encoding="utf-8", errors="replace"), plan_path, task, frozen_copy)
                    if status == "owned":
                        active.append(path)
                    else:
                        destination = contradictions if status == "foreign" else unchecked
                        destination.extend(str(path) + ": " + reason for reason in reasons)
            except OSError as error:
                unchecked.append("cannot read working-cycle path %s: %s" % (path, error))
        candidates = commits_touching(git, observation.refs, archive)
        snapshots = {}
        for commit in candidates:
            paths = archived_files(git, commit, archive)
            if not paths:
                continue  # Deletion alone cannot supply a record; earlier snapshots remain visible.
            cache = {}

            def read(name):
                if name not in cache:
                    cache[name] = git.run("show", commit + ":" + name).stdout.decode(
                        "utf-8", errors="replace")
                return cache[name]

            status, records, reasons = provenance(paths, read, plan_path, task, frozen_copy)
            if status != "owned":
                destination = contradictions if status == "foreign" else unchecked
                destination.extend("commit " + commit + ": " + reason for reason in reasons)
                continue
            archived.append(commit)
            snapshots[commit] = records
            refs = git.text("for-each-ref", "--contains=" + commit, "--format=%(refname)",
                            "refs/heads/", "refs/remotes/")
            lines.append("evidence %s: archived cycle %s commit %s on %s" %
                         (prefix, archive, commit, display(", ".join(refs.splitlines()))))
            for source, link in record_pointers(git, commit, records):
                lines.append("evidence %s: PR pointer from %s: %s" %
                             (prefix, display(source), display(link)))
        # A deletion is a cycle trace, but cannot stand for actual archived content.
        if observation.commit and observation.complete:
            for commit in commits_touching(git, [observation.commit], archive):
                paths = snapshots.get(commit, [])
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
    conflict = bool(contradictions)
    for reason in contradictions:
        lines.append("conflict %s: %s; human reconciliation required" % (prefix, display(reason)))
    if conflict:
        pass
    elif task.state in ("ready for cycle", "in cycle"):
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
    # Redirected Windows streams can inherit ANSI, which cannot preserve path evidence.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="strict")
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
            lines, conflict, failure = task_report(git, observation, task, plan_path)
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
