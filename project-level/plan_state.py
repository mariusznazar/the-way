"""Read evidence for project-plan progress without changing project documents (WAY-153).

Usage: python -B <the-way>/project-level/plan_state.py PLAN PRODUCT_REPOSITORY

Exit codes: 0 for a completed observation (unchecked evidence can remain) or for a closed plan,
1 for source findings or conflicting task states, 2 for invocation, source-read or Git operational
errors. A plan whose `Status:` line reads `closed YYYY-MM-DD` and whose tasks all stand in a final
state is reported closed, and no Git evidence is read for it. Only Git metadata is refreshed;
proposals never apply changes to the plan or task documents.
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
PR_LINK = re.compile(
    r"https?://[^\s<>\[\]()`\"']+/(?:pull|merge_requests)/[0-9]+"
    r"(?:[?#][^\s<>\[\]()`\"']*)?"
)
# The wording of the field `Request URL and status` in a record committed before its request exists
# (task-cycle/skill/reserved_return.md, blocked_finding.md): the whole line, nothing else.
BLOCKED_DRAFT = "- Request URL and status: blocked draft, opened on this commit"


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
            result = subprocess.run(
                ["git", "-C", str(self.repository), *arguments],
                capture_output=True,
                timeout=GIT_TIMEOUT,
                env=environment,
            )
        except (OSError, subprocess.TimeoutExpired) as error:
            raise GitError("git %s: %s" % (arguments[0], display(error))) from error
        if result.returncode not in allowed:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise GitError(
                "git %s failed (%d): %s" % (arguments[0], result.returncode, display(detail))
            )
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
            observation.unchecked.append(
                "origin remote unavailable; integration is not established"
            )
        else:
            route = git.run("symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", allowed=(0, 1))
            ref = route.stdout.decode("utf-8").strip()
            if (
                route.returncode
                or not ref.startswith("refs/remotes/origin/")
                or ref.endswith("/HEAD")
            ):
                observation.unchecked.append(
                    "origin/HEAD does not establish one integration branch"
                )
            else:
                branch = ref[len("refs/remotes/origin/") :]
                remote_head = git.text("ls-remote", "--symref", "origin", "HEAD")
                declared = [
                    line.split("\t")[0][5:]
                    for line in remote_head.splitlines()
                    if line.startswith("ref: ") and line.endswith("\tHEAD")
                ]
                if declared != ["refs/heads/" + branch]:
                    observation.unchecked.append(
                        "origin/HEAD disagrees with the remote default or "
                        "the remote has no unambiguous HEAD"
                    )
                else:
                    git.run("fetch", "--no-tags", "origin", "+refs/heads/*:refs/remotes/origin/*")
                    commit = git.text("rev-parse", "--verify", ref + "^{commit}")
                    observation.integration, observation.commit = ref, commit
    except (GitError, UnicodeError) as error:
        observation.errors.append(display(error))
        observation.complete = False
    try:
        # Tags and detached HEADs do not declare branches. Symbolic remote HEAD is redundant.
        refs = git.text(
            "for-each-ref", "--format=%(refname) %(symref)", "refs/heads/", "refs/remotes/"
        )
        observation.refs = [line.split()[0] for line in refs.splitlines() if len(line.split()) == 1]
    except (GitError, UnicodeError) as error:
        observation.errors.append(display(error))
        observation.complete = False
    return observation


def commits_touching(git, refs, path):
    if not refs:
        return []
    return git.text(
        "log", "--full-history", "--format=%H", *refs, "--", ":(literal)" + path
    ).splitlines()


def archived_files(git, commit, archive):
    """Inventory ordinary blobs without following symlinks or imposing record basenames."""
    raw = git.run("ls-tree", "-r", "-z", "--full-tree", commit, "--", ":(literal)" + archive).stdout
    paths = []
    for entry in raw.split(b"\0"):
        if entry:
            metadata, path = entry.split(b"\t", 1)
            mode, kind, _ = metadata.split()
            if mode.startswith(b"100") and kind == b"blob":
                paths.append(path.decode("utf-8"))
    return paths


def record_requests(git, commit, paths):
    """Read request evidence of records as data, in one Git read, without printing their text.

    Returns the sorted pull-request pointers as (source, link) and the sorted record paths whose
    field `Request URL and status` reads exactly BLOCKED_DRAFT; nothing else of a record is kept.

    Limit: the lines are read as text, with no Markdown structure, so a pointer or the wording
    inside a fenced code block is read as the field; the pointer lines have the same limit. Lines
    end at `\\n` only; a lone `\\r` is part of its line, so a line that carries anything
    after the wording but spaces, tabs and the `\\r` of a CRLF ending is not the field.
    """
    # BLOCKED_DRAFT holds no ERE metacharacter, so it is its own pattern: `re.escape` would add
    # backslashes before `-` and a space, which POSIX ERE leaves undefined.
    result = git.run(
        "grep",
        "-I",
        "-z",
        "-n",
        "-E",
        "-e",
        r"https?://[^ ]+/(pull|merge_requests)/[0-9]+",
        "-e",
        BLOCKED_DRAFT,
        commit,
        "--",
        *(":(literal)" + path for path in paths),
        allowed=(0, 1),
    )
    pointers, blocked = [], []
    for row in result.stdout.split(b"\n"):
        parts = row.split(b"\0", 2)
        if len(parts) == 3:
            source = parts[0].decode("utf-8")
            text = parts[2].decode("utf-8", errors="replace")
            for link in PR_LINK.findall(text):
                pointers.append((source, link))
            if text.rstrip(" \t\r") == BLOCKED_DRAFT and source.startswith(commit + ":"):
                blocked.append(source[len(commit) + 1 :])
    return sorted(set(pointers)), sorted(set(blocked))


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
        yield value[: separator.start()]
    yield value


def frozen_link(document):
    """Read a Document link to a task's frozen copy as a product commit and path, or None."""
    link = re.fullmatch(
        r"https?://[^/\s]+/\S*?/(?:-/)?blob/([0-9a-f]{7,40})/([^?#\s]+)(?:[?#]\S*)?",
        path_value(document),
    )
    if not link or any(not char.isprintable() for char in unquote(link[2])):
        return None
    return link[1], unquote(link[2])


def bare_name(value):
    name = path_value(value)
    return "/" not in name and "\\" not in name


def names_plan(value, parents, plan_path):
    """Accept a plan path relative to a task document's folder or the plan's bare file name."""
    if bare_name(value) and os.path.normcase(path_value(value)) == os.path.normcase(
        os.path.basename(plan_path)
    ):
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


def anchored_parents(path, source, document, task, frozen_copy):
    """The folders a record's task documents may stand in, anchored at its original source, as
    (parents, None); where the source cannot be anchored or is another task's, (None, problem)
    with the problem as (kind, message)."""
    candidates = [
        candidate for candidate in map(source_path, leading_values(source)) if candidate is not None
    ]
    if frozen_copy is None:
        if not candidates or document is None or task.document == "—":
            return None, (
                "unresolved",
                path + ": original Task source or Document cannot be anchored",
            )
        if document not in candidates:
            return None, (
                "foreign",
                path + ": Task source " + source + " differs from Document " + document,
            )
        return [Path(document).parent], None
    # The source document is gone; any folder its recorded path may name can hold it.
    return [Path(candidate).parent for candidate in candidates], None


def relation_problem(path, relation_text, parents, plan_path, task, frozen_copy):
    """None where a record's Task relation names this plan's item of the task, else the problem as
    (kind, message)."""
    if not re.match(r"plan item(?![\w-])", relation_text):
        return (
            "unresolved",
            path + ": same-source Task relation does not establish this plan's membership",
        )
    # The frozen task binds plan and name below; only the one expanded form also names them.
    relation = re.fullmatch(
        r"plan item — (.+?) \([^\n]+\), item ([1-9][0-9]*) "
        r"([a-z0-9]+(?:-[a-z0-9]+)*)(?:; .+)?",
        relation_text,
    )
    if not relation:
        return None
    related_plan = source_path(relation[1], parents[0]) if parents else relation[1]
    if names_plan(relation[1], parents, plan_path) and relation[3] == task.name:
        return None
    if unsure(relation[1], frozen_copy) and relation[3] == task.name:
        return (
            "unresolved",
            path + ": Task relation's plan cannot be resolved without the removed source document",
        )
    return (
        "foreign",
        path
        + ": Task relation names plan "
        + str(related_plan)
        + " item "
        + relation[2]
        + " "
        + relation[3],
    )


def frozen_artifact_problem(path, paths, read, text, parents, plan_path, task, frozen_copy):
    """None where a record's frozen task artifact stands in its cycle snapshot and names this plan
    and task, else the problem as (kind, message)."""
    artifacts = re.search(r"^## Artifacts\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    frozen = []
    if artifacts:
        for line in artifacts[1].splitlines():
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0].lower() == "frozen task":
                frozen.append(cells[1])
    if len(frozen) != 1:
        return "unresolved", path + ": missing or ambiguous frozen task artifact"
    # Frozen artifacts must belong to this snapshot, not today's external source or another cycle.
    targets = {
        posixpath.normpath(
            posixpath.join(posixpath.dirname(path), path_value(value).replace("\\", "/"))
        )
        for value in leading_values(frozen[0])
        if path_value(value)
    } & set(paths)
    if len(targets) != 1:
        return "unresolved", path + ": frozen task artifact absent from this cycle snapshot"
    target = targets.pop()
    if frozen_copy is not None and read(target).replace("\r\n", "\n") != frozen_copy.replace(
        "\r\n", "\n"
    ):
        return "foreign", path + ": frozen task differs from the frozen copy the Document links"
    memberships = header_fields(read(target), "Project relation")
    if len(memberships) != 1:
        return "unresolved", path + ": missing or ambiguous frozen task membership"
    membership = re.fullmatch(r"plan item: (.+) — ([a-z0-9]+(?:-[a-z0-9]+)*)", memberships[0])
    if not membership:
        return "unresolved", path + ": frozen task membership cannot be read"
    member_plan = source_path(membership[1], parents[0]) if parents else membership[1]
    if names_plan(membership[1], parents, plan_path) and membership[2] == task.name:
        return None
    if unsure(membership[1], frozen_copy) and membership[2] == task.name:
        return (
            "unresolved",
            path + ": frozen task's plan cannot be resolved without the removed source document",
        )
    return (
        "foreign",
        path
        + ": frozen task names plan "
        + str(member_plan)
        + " task "
        + membership[2]
        + ", not the supplied plan/task",
    )


def record_provenance(path, paths, read, plan_path, task, frozen_copy, document):
    """Judge one record of a cycle: ("skip", None) where it holds no provenance field, ("owned",
    None) where it belongs to the task, else ("unresolved" or "foreign", the reason)."""
    text = read(path)
    sources = header_fields(text, "Task source")
    relations = header_fields(text, "Task relation")
    if not sources and not relations:
        return "skip", None
    if len(sources) != 1 or len(relations) != 1:
        return "unresolved", path + ": missing or ambiguous task provenance fields"
    if frozen_copy is False:
        return (
            "unresolved",
            path + ": frozen copy the Document links is absent from the product repository",
        )
    parents, problem = anchored_parents(path, sources[0], document, task, frozen_copy)
    if problem:
        return problem
    problem = relation_problem(path, relations[0], parents, plan_path, task, frozen_copy)
    if problem:
        return problem
    problem = frozen_artifact_problem(
        path, paths, read, text, parents, plan_path, task, frozen_copy
    )
    return problem or ("owned", None)


def provenance(paths, read, plan_path, task, frozen_copy=None):
    """Associate each record with its own retained task, anchored at its original source.

    A Document linking the task's frozen copy anchors records by that copy's text instead
    (frozen_copy); False marks a linked copy the product repository cannot supply.
    """
    document = source_path(task.document, Path(plan_path).parent)
    owned, unresolved, foreign = [], [], []
    for path in paths:
        kind, reason = record_provenance(path, paths, read, plan_path, task, frozen_copy, document)
        if kind == "owned":
            owned.append(path)
        elif kind == "unresolved":
            unresolved.append(reason)
        elif kind == "foreign":
            foreign.append(reason)
    if foreign:
        return "foreign", owned, foreign
    if unresolved:
        return "unchecked", [], unresolved
    if not owned:
        return "unchecked", [], ["missing recorded task provenance in cycle snapshot"]
    return "owned", owned, []


@dataclass
class TaskEvidence:
    """What the report on one task has found so far: its lines, the evidence of each kind, and
    the reasons the evidence cannot be established or contradicts the plan."""

    prefix: str
    lines: list = field(default_factory=list)
    active: list = field(default_factory=list)
    archived: list = field(default_factory=list)
    merged: list = field(default_factory=list)
    unchecked: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    contradictions: list = field(default_factory=list)


def archived_cycles(git, observation, task, plan_path, frozen_copy, archive, evidence):
    """Read the cycle records each commit that touches the task's archive directory holds, and
    note those that belong to the task in `evidence`. Return the record paths of each such
    commit."""
    prefix = evidence.prefix
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
                    "utf-8", errors="replace"
                )
            return cache[name]

        status, records, reasons = provenance(paths, read, plan_path, task, frozen_copy)
        if status != "owned":
            destination = evidence.contradictions if status == "foreign" else evidence.unchecked
            destination.extend("commit " + commit + ": " + reason for reason in reasons)
            continue
        evidence.archived.append(commit)
        snapshots[commit] = records
        refs = git.text(
            "for-each-ref",
            "--contains=" + commit,
            "--format=%(refname)",
            "refs/heads/",
            "refs/remotes/",
        )
        evidence.lines.append(
            "evidence %s: archived cycle %s commit %s on %s"
            % (prefix, archive, commit, display(", ".join(refs.splitlines())))
        )
        pointers, blocked = record_requests(git, commit, records)
        for source, link in pointers:
            evidence.lines.append(
                "evidence %s: PR pointer from %s: %s" % (prefix, display(source), display(link))
            )
        for record in blocked:
            evidence.lines.append(
                "evidence %s: blocked draft request in record %s commit %s"
                % (prefix, display(record), commit)
            )
    return snapshots


def report_verdict(observation, task, evidence):
    """The lines that close the report on a task: its working cycles, the conflicts, the proposed
    moves and what stays unchecked. Return the lines, whether the task conflicts and whether an
    error stopped the reading."""
    prefix, lines = evidence.prefix, evidence.lines
    unchecked = evidence.unchecked
    for path in evidence.active:
        lines.append("evidence %s: working cycle %s" % (prefix, display(path)))
    trace = bool(evidence.active or evidence.archived or evidence.merged)
    conflict = bool(evidence.contradictions)
    for reason in evidence.contradictions:
        lines.append("conflict %s: %s; human reconciliation required" % (prefix, display(reason)))
    if conflict:
        pass
    elif task.state in ("ready for cycle", "in cycle"):
        if task.state == "ready for cycle" and trace:
            lines.append("propose %s: ready for cycle -> in cycle" % prefix)
        if evidence.merged and not evidence.errors:
            lines.append("propose %s: in cycle -> done" % prefix)
        else:
            unchecked.append(
                "PR outcome unchecked; cycle evidence is outside established fresh "
                "integration history"
                if trace
                else "no sufficient cycle trace; PR outcome unchecked"
            )
    elif trace and (
        task.state != "done"
        or evidence.active
        or (
            observation.commit
            and observation.complete
            and not evidence.merged
            and not evidence.errors
        )
    ):
        conflict = True
        lines.append(
            "conflict %s: cycle trace conflicts with plan state %s; human reconciliation "
            "required" % (prefix, task.state)
        )
    elif task.state == "done" and not evidence.merged:
        unchecked.append(
            "plan says done but completion cannot be established from fresh Git history"
        )
    elif not trace:
        unchecked.append("no sufficient cycle trace; no progress inferred")
    for reason in observation.unchecked + unchecked:
        lines.append("unchecked %s: %s" % (prefix, display(reason)))
    for error in evidence.errors:
        lines.append("error: " + error)
    return lines, conflict, bool(evidence.errors)


def task_report(git, observation, task, plan_path):
    prefix = "%d %s" % (task.number, task.name)
    evidence = TaskEvidence(prefix, ["task %s: %s" % (prefix, task.state)])
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
                    files = [
                        file
                        for file in path.rglob("*")
                        if file.is_file()
                        and not any(parent.is_symlink() for parent in (file, *file.parents))
                    ]
                    paths = [file.relative_to(path).as_posix() for file in files]
                    status, _, reasons = provenance(
                        paths,
                        lambda name: (path / name).read_text(encoding="utf-8", errors="replace"),
                        plan_path,
                        task,
                        frozen_copy,
                    )
                    if status == "owned":
                        evidence.active.append(path)
                    else:
                        destination = (
                            evidence.contradictions if status == "foreign" else evidence.unchecked
                        )
                        destination.extend(str(path) + ": " + reason for reason in reasons)
            except OSError as error:
                evidence.unchecked.append("cannot read working-cycle path %s: %s" % (path, error))
        snapshots = archived_cycles(
            git, observation, task, plan_path, frozen_copy, archive, evidence
        )
        # A deletion is a cycle trace, but cannot stand for actual archived content.
        if observation.commit and observation.complete:
            for commit in commits_touching(git, [observation.commit], archive):
                paths = snapshots.get(commit, [])
                if paths:
                    evidence.merged.append(commit)
                    evidence.lines.append(
                        "evidence %s: cycle record %s commit %s reachable from %s %s"
                        % (
                            prefix,
                            display(", ".join(paths)),
                            commit,
                            observation.integration,
                            observation.commit,
                        )
                    )
    except (GitError, UnicodeError) as error:
        evidence.errors.append(display(error))
        evidence.merged = []
    return report_verdict(observation, task, evidence)


def sources(plan_path):
    """Validate original whole sources with the existing checkers, then reuse their parser."""
    text, error = plan_check.read(plan_path)
    if error:
        return None, ["error: " + display(error)], 2, None
    relative = plan_check.definition_path(text)
    definition, error = None, None
    if relative is not None:
        definition, error = plan_check.read(os.path.join(os.path.dirname(plan_path), relative))
        if error:
            return None, ["error: " + display(error)], 2, None
    findings = [str(finding) for finding in plan_check.check(text, definition, error)]
    preamble, sections = plan_check.split(text)
    statuses = [line.rstrip() for _, line in preamble if line.startswith("Status:")]
    closed = plan_check.closed_date(preamble)
    if not closed and (len(statuses) != 1 or not statuses[0].startswith("Status: handed over ")):
        findings.append("fail: plan must have one handed-over Status line")
    if definition is not None:
        findings.extend(
            "definition " + str(finding) for finding in readiness_check.check(definition)
        )
        header, _ = readiness_check.split(definition)
        approvals = [line.rstrip() for _, line in header if line.startswith("Status:")]
        if len(approvals) != 1 or not re.fullmatch(
            r"Status: approved [0-9]{4}-[0-9]{2}-[0-9]{2}", approvals[0]
        ):
            findings.append("fail: definition must have one approved Status line")
        elif not plan_check.calendar_date(approvals[0][-10:]):
            findings.append("fail: definition approval date is not a calendar date")
    if findings:
        return None, findings, 1, None
    section = next(section for section in sections if section.name == plan_check.TASKS)
    _, tasks, _ = plan_check.read_tasks(section)
    return tasks, [], 0, closed


def main(argv=None):
    # surface: project-plan-state-command — pinned
    # Redirected Windows streams can inherit ANSI, which cannot preserve path evidence.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(
        description="Report Git evidence for project plan task states."
    )
    parser.add_argument("plan", help="original handed-over or closed project plan")
    parser.add_argument("product_repository", help="product Git repository")
    args = parser.parse_args(argv)
    try:
        plan_path = os.path.abspath(args.plan)
        repository = Path(args.product_repository).resolve()
        tasks, findings, code, closed = sources(plan_path)
        for finding in findings:
            print(display(finding))
        if code:
            return code
        if closed:
            print("closed: the plan was closed on %s; its tasks stand in final states" % closed)
            return 0
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
