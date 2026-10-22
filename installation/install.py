"""Prepare a product repository to use one pinned commit of the-way."""

from __future__ import annotations

import argparse
import difflib
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit


SOURCE = Path(__file__).resolve().parent.parent
SUBMODULE = ".the-way"
ELEMENTS = {
    "decisions": ("record-decision", "decisions.md"),
    "invariants": ("record-invariant", "invariants.md"),
    "glossary": ("record-glossary-term", "glossary.md"),
    "part-map": ("update-part-map", "part_map.md"),
    "environment-facts": ("record-environment-fact", "environment_facts.md"),
}
SKILLS = {
    name: f"elements/{element}/skill/SKILL.md"
    for element, (name, _) in ELEMENTS.items()
}
SKILLS.update({
    "find-foundation-entries": "elements/common/skill/SKILL.md",
    "define-project": "project-level/skill/SKILL.md",
    "plan-project": "project-level/plan/skill/SKILL.md",
    "lead-project": "project-level/lead/skill/SKILL.md",
    "settle-technology": "project-level/technology/SKILL.md",
    "refine-task": "project-level/task/skill/SKILL.md",
    "implement-task": "task-cycle/skill/SKILL.md",
    "plan-task": "task-cycle/plan/SKILL.md",
    "write-spec": "task-cycle/spec/SKILL.md",
    "make-change": "task-cycle/change/SKILL.md",
    "review-change": "task-cycle/review/SKILL.md",
    "critique": "elements/common/critique/SKILL.md",
    "maintain-styleguide": "product-guidelines/styleguide/SKILL.md",
    "maintain-coding-guidelines": "product-guidelines/coding/SKILL.md",
})
# Claude Code reads project skills from .claude/skills, Codex from .agents/skills.
SKILL_DIRECTORIES = (".claude", ".agents")
CLAUDE = "CLAUDE.md"
CLAUDE_IMPORT = "@AGENTS.md\n"
AGENTS = "AGENTS.md"
BEGIN = "<!-- the-way:begin -->"
END = "<!-- the-way:end -->"
IGNORE = ".gitignore"
RUNS = ".runs/"
# Every entry point the installer writes says this, whatever commit wrote it; a file at an entry
# point's path that does not is the product's own.
OWN_MARK = f"The process for this repository is pinned as the Git submodule `{SUBMODULE}`"
OWN_DESCRIPTION = " Use this product's pinned the-way commit."
# Codex reads AGENTS.override.md instead of AGENTS.md, and at most this many bytes of them.
CODEX_OVERRIDE = "AGENTS.override.md"
CODEX_LIMIT = 32 * 1024


# Set by run() only when the submodule URL is a local path or a file:// URL.
FILE_PROTOCOL: list[str] = []


def is_local(url: str) -> bool:
    return url.startswith("file://") or Path(url).exists()


def git(*args: str, cwd: Path, check: bool = True,
        stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(["git", *FILE_PROTOCOL, *args], cwd=cwd, input=stdin,
                            text=True, encoding="utf-8", stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result


def committed(path: str, commit: str) -> str:
    return git("show", f"{commit}:{path}", cwd=SOURCE).stdout


def empty_foundations() -> dict[str, str]:
    return {
        "decisions.md": "# Decision log\n",
        "invariants.md": (
            "# Invariants\n\n"
            "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
        ),
        "glossary.md": "# Glossary\n\nTerms used by this product's foundation.\n",
        "part_map.md": (
            "# Part map\n\n"
            "## External context\n\n"
            "| Partner | Direction | What comes in |\n"
            "|---|---|---|\n\n"
            "## Files left out on purpose\n\n| File | Why |\n|---|---|\n\n"
            "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
        ),
        "environment_facts.md": (
            "# Environment facts\n\n"
            "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
        ),
    }


def sibling_names() -> str:
    names = [f"`{name}`" for name in SKILLS]
    return ", ".join(names[:-1]) + " or " + names[-1]


def skill_wrapper(path: str, name: str, commit: str) -> str:
    """The entry point of one skill, with its description at `commit`. It names no commit, since
    the gitlink records it; the installer rewrites it whenever a moved pin reads differently."""
    original = committed(path, commit)
    original_name = re.search(r"^name: (.+)$", original, re.M)
    if not original_name or original_name.group(1) != name:
        raise RuntimeError(f"Unexpected skill name for {path} at {commit}")
    description = re.search(r"^description: (.+)$", original, re.M)
    if not description:
        raise RuntimeError(f"Missing skill description for {path}")
    project_name = f"the-way-{name}"
    return (f"---\nname: {project_name}\n"
            f"description: {description.group(1)}{OWN_DESCRIPTION}\n"
            "---\n\n"
            f"# {project_name}\n\n"
            f"{OWN_MARK}, at the commit its gitlink records.\n\n"
            f"If `{SUBMODULE}/{path}` is absent, run "
            f"`git submodule update --init -- {SUBMODULE}` from the product root. "
            f"Check `git ls-files --stage -- {SUBMODULE}` and "
            f"`git -C {SUBMODULE} rev-parse HEAD`: both must show the same commit. "
            "If initialization fails or the commits differ, stop.\n\n"
            f"Read `{SUBMODULE}/{path}` in full and follow it. "
            f"Read the files it references inside `{SUBMODULE}`. "
            "Where it says where the-way lies, the product's case applies: "
            f"here the process root is `{SUBMODULE}`. Do not substitute a global skill.\n\n"
            f"Where this skill or a file it reads names another the-way skill — {sibling_names()} "
            "— use this product's project skill of the same name with the `the-way-` prefix, "
            "never an unprefixed one.\n")


def product_guidance() -> str:
    """The guidance for agents in a product, which the installer keeps between its markers in
    AGENTS.md. It names no commit, since the gitlink records it; the installer rewrites it in place
    whenever a moved pin's guidance reads differently."""
    names = ", ".join(f"`the-way-{name}`" for name, _ in ELEMENTS.values())
    other_names = ", ".join(f"`the-way-{name}`" for name in SKILLS if name not in
                            {entry_name for entry_name, _ in ELEMENTS.values()})
    return ("# Pinned the-way process\n\n"
            "This repository uses the-way, the process for its foundation, at the commit the "
            f"gitlink of the Git submodule `{SUBMODULE}` records. After a fresh clone run "
            f"`git submodule update --init -- {SUBMODULE}`; it needs read access to the Git URL in "
            f"`.gitmodules`. Before use, `git -C {SUBMODULE} rev-parse HEAD` must show the commit "
            f"`git ls-files --stage -- {SUBMODULE}` records. If initialization fails or the commits "
            "differ, stop; never use another copy or version of the-way.\n\n"
            f"Write foundation entries only through the project skills {names}. Use the project "
            f"skills {other_names} for their named work. Where a skill or "
            "a file it reads names one without the `the-way-` prefix, use the prefixed project "
            "skill, never a personal skill of that name. In a task cycle the methods of the-way "
            "apply — `the-way-write-spec`, `the-way-plan-task`, `the-way-make-change` and "
            "`the-way-review-change` — even where an installed plugin offers methods of its own."
            "\n\n"
            f"Run the-way's scripts from this repository's root as `{SUBMODULE}/<path>`. There "
            f"`python -B {SUBMODULE}/elements/common/foundation_check.py` checks this repository's "
            "foundation, its guidelines and the part each file git tracks belongs to. The skills "
            f"of the-way keep their working files under `{RUNS}`, which `.gitignore` must keep "
            "ignored.\n\n"
            "Until the part map has its first parts, `foundation_check.py` reports every file git "
            "tracks as claimed by no part; that is expected, and it is not a pass. The first map "
            "is written with `the-way-update-part-map`.\n\n"
            "Before a merge, run every test of this repository with its one command, which "
            f"runs `python -B {SUBMODULE}/elements/common/foundation_check.py` too, and report "
            "what failed and what stayed unchecked. While the one command does not run "
            "that check, run it on its own and report the check as left unchecked by the one "
            "command. A check that did not run is never a pass.\n")


def agents_block() -> str:
    return f"{BEGIN}\n{product_guidance()}{END}\n"


def read_text_file(path: Path, name: str) -> str:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"Existing {name} is not a regular file")
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as error:
        raise RuntimeError(f"Existing {name} is not UTF-8 text") from error


def has_agents_import(text: str) -> bool:
    """Recognize the root import outside Markdown fenced blocks and code spans."""
    prose = []
    fence = None
    for line in text.splitlines(keepends=True):
        if fence:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) +
                            "{" + str(len(fence)) + r",}[ \t]*(?:\r?\n)?", line):
                fence = None
            prose.append("\n")
            continue
        opening = re.match(r" {0,3}(`{3,}|~{3,})(.*)", line)
        if opening and (opening[1][0] != "`" or "`" not in opening[2]):
            fence = opening[1]
            prose.append("\n")
        else:
            prose.append(line)
    outside_code = re.sub(r"(?<!`)(`+)(?!`)[\s\S]*?(?<!`)\1(?!`)", " ", "".join(prose))
    return re.search(r"(?<!\S)@AGENTS\.md(?=\s|$)", outside_code) is not None


def claude_change(path: Path) -> tuple[str, str]:
    if not os.path.lexists(path):
        return "CREATE", CLAUDE_IMPORT
    read_text_file(path, CLAUDE)
    return "KEEP", ""


def appended(text: str, addition: str, blank_line: bool) -> str:
    """What to append to an existing text so that `addition` starts on its own line, after a
    blank line when asked, in the file's own line ending."""
    normal = text.replace("\r\n", "\n")
    if not normal or normal.endswith("\n\n") or (normal.endswith("\n") and not blank_line):
        separator = ""
    elif normal.endswith("\n"):
        separator = "\n"
    else:
        separator = "\n\n" if blank_line else "\n"
    return (separator + addition).replace("\n", "\r\n" if "\r\n" in text else "\n")


def agents_change(path: Path) -> tuple[str, str]:
    """CREATE, APPEND, KEEP or REPLACE the marked block of the product guidance in AGENTS.md.
    REPLACE carries the whole new text: the block rewritten where it stands, in the file's own
    line ending, and everything outside the markers byte for byte."""
    block = agents_block()
    if not os.path.lexists(path):
        return "CREATE", block
    text = read_text_file(path, AGENTS)
    normal = text.replace("\r\n", "\n")
    begins, ends = normal.count(BEGIN), normal.count(END)
    if begins == ends == 0:
        return "APPEND", appended(text, block, blank_line=True)
    if begins == ends == 1 and normal.index(BEGIN) < normal.index(END):
        if normal[normal.index(BEGIN):normal.index(END) + len(END)] == block[:-1]:
            return "KEEP", ""
        newline = "\r\n" if "\r\n" in text else "\n"
        start, end = text.index(BEGIN), text.index(END) + len(END)
        return "REPLACE", text[:start] + block[:-1].replace("\n", newline) + text[end:]
    raise RuntimeError(f"{AGENTS} holds {begins} {BEGIN} and {ends} {END} markers; it must hold "
                       "one complete block or none. Fix it by hand and run again")


def ignore_change(path: Path) -> tuple[str, str]:
    """CREATE .gitignore or APPEND the line that ignores the-way's records of a run."""
    if not os.path.lexists(path):
        return "CREATE", RUNS + "\n"
    text = read_text_file(path, IGNORE)
    if RUNS in text.replace("\r\n", "\n").split("\n"):
        return "KEEP", ""
    return "APPEND", appended(text, RUNS + "\n", blank_line=False)


def inside_repo(target: Path) -> None:
    root = Path(git("rev-parse", "--show-toplevel", cwd=target).stdout.strip()).resolve()
    if root != target:
        raise RuntimeError(f"Target must be the repository root: {root}")
    if target == SOURCE:
        raise RuntimeError("The product repository must be separate from the-way")


def existing_pin(target: Path) -> str | None:
    result = git("ls-files", "--stage", "--", SUBMODULE, cwd=target).stdout.strip()
    if not result:
        return None
    fields = result.split()
    if len(fields) != 4 or fields[0] != "160000" or fields[3] != SUBMODULE:
        raise RuntimeError(f"{SUBMODULE} exists in the index but is not a Git submodule")
    return fields[1]


def check_parents(target: Path, path: Path) -> None:
    parent = path.parent
    while parent != target:
        if os.path.lexists(parent) and (parent.is_symlink() or not parent.is_dir()):
            raise RuntimeError(f"Parent path is not a regular directory: {parent}")
        parent = parent.parent


def owned_entry_point(path: Path) -> bool:
    """Whether the file at an entry point's path is one the installer wrote, at this commit or
    an earlier one: a regular UTF-8 file whose header names the skill of its directory with the
    `the-way-` prefix, whose description ends as the installer ends it, and which points to the
    pinned submodule."""
    if path.is_symlink() or not path.is_file():
        return False
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return False
    header = re.match(r"---\r?\nname: (.+?)\r?\ndescription: (.+?)\r?\n---\r?\n", text)
    return bool(header and header.group(1) == path.parent.name and
                path.parent.name.startswith("the-way-") and
                header.group(2).endswith(OWN_DESCRIPTION) and OWN_MARK in text)


def stale_entry_points(target: Path) -> list[Path]:
    """The installer's entry points of skills this commit of the-way no longer has. An entry
    point the installer did not write stays, whatever its name."""
    stale = []
    for directory in SKILL_DIRECTORIES:
        skills = target / directory / "skills"
        if skills.is_symlink() or not skills.is_dir():
            continue
        for entry in sorted(skills.iterdir()):
            name = entry.name.removeprefix("the-way-")
            if entry.name.startswith("the-way-") and name not in SKILLS and \
                    not entry.is_symlink() and owned_entry_point(entry / "SKILL.md"):
                stale.append(entry / "SKILL.md")
    return stale


def verify_remote(url: str, commit: str) -> None:
    with tempfile.TemporaryDirectory(prefix="the-way-pin-") as temporary:
        mirror = Path(temporary) / "source"
        git("clone", "--quiet", "--no-checkout", "--", url, str(mirror), cwd=SOURCE)
        found = git("cat-file", "-e", f"{commit}^{{commit}}", cwd=mirror, check=False)
        if found.returncode:
            git("fetch", "--quiet", "origin", commit, cwd=mirror, check=False)
            found = git("cat-file", "-e", f"{commit}^{{commit}}", cwd=mirror, check=False)
        if found.returncode:
            raise RuntimeError(f"Commit {commit} is not available from {url}; publish it first")


def plan(target: Path, commit: str, url: str) -> tuple[
        dict[Path, str], dict[Path, tuple[str, str]], list[Path], bool, bool, str | None]:
    """What the run does: the files the installer owns, the shared files, the entry points it
    deletes, whether it adds or initializes the submodule, and the pin it moves from, if any."""
    files: dict[Path, str] = {}
    for filename, content in empty_foundations().items():
        files[target / "foundations" / filename] = content
    for name, path in SKILLS.items():
        wrapper = skill_wrapper(path, name, commit)
        for directory in SKILL_DIRECTORIES:
            files[target / directory / "skills" / f"the-way-{name}" / "SKILL.md"] = wrapper
    shared = {target / AGENTS: agents_change(target / AGENTS),
              target / IGNORE: ignore_change(target / IGNORE),
              target / CLAUDE: claude_change(target / CLAUDE)}

    pin = existing_pin(target)
    submodule_path = target / SUBMODULE
    modules_file = target / ".gitmodules"
    if pin:
        configured = git("config", "-f", str(modules_file), "--get",
                         f"submodule.{SUBMODULE}.url", cwd=target, check=False)
        if configured.returncode or configured.stdout.strip() != url:
            raise RuntimeError(f"Existing {SUBMODULE} has a different URL in .gitmodules")
        if submodule_path.is_symlink() or (submodule_path.exists() and not submodule_path.is_dir()):
            raise RuntimeError(f"Existing {SUBMODULE} is not a submodule directory")
        if submodule_path.is_dir() and not os.path.lexists(submodule_path / ".git") and \
                any(submodule_path.iterdir()):
            raise RuntimeError(f"Uninitialized {SUBMODULE} contains other files")
    elif os.path.lexists(submodule_path):
        raise RuntimeError(f"{submodule_path} already exists; refusing to replace it")
    elif ignored_paths(target, [submodule_path]):
        # `git submodule add` refuses an ignored path, so the run could not finish.
        raise RuntimeError(f"Git ignores {SUBMODULE} in this repository, so the submodule cannot "
                           f"be added; stop ignoring {SUBMODULE} and run again")
    elif os.path.lexists(modules_file):
        if modules_file.is_symlink() or not modules_file.is_file():
            raise RuntimeError("Existing .gitmodules is not a regular file")
        if git("ls-files", "--error-unmatch", "--", ".gitmodules", cwd=target,
               check=False).returncode:
            raise RuntimeError("Existing .gitmodules is not tracked; refusing to stage it")
        if git("diff", "--quiet", "--", ".gitmodules", cwd=target, check=False).returncode or \
                git("diff", "--cached", "--quiet", "--", ".gitmodules", cwd=target,
                    check=False).returncode:
            raise RuntimeError("Existing .gitmodules has uncommitted changes")
        registered = git("config", "-f", str(modules_file), "--get-regexp",
                         r"^submodule\..*\.path$", cwd=target, check=False)
        if registered.returncode not in (0, 1):
            raise RuntimeError("Cannot parse the existing .gitmodules")
        if any(line.split(" ", 1)[-1] == SUBMODULE for line in registered.stdout.splitlines()):
            raise RuntimeError(f".gitmodules already registers {SUBMODULE}")

    for path, expected in files.items():
        check_parents(target, path)
        if not os.path.lexists(path):
            continue
        if path.parts[-2] == "foundations":
            if not path.is_file() or path.is_symlink():
                raise RuntimeError(f"Existing foundation path is not a regular file: {path}")
        elif not owned_entry_point(path):
            raise RuntimeError(f"Existing integration file differs: {path}")
    if pin and os.path.lexists(submodule_path / ".git"):
        checked_out = git("-C", SUBMODULE, "rev-parse", "HEAD", cwd=target).stdout.strip()
        if checked_out != pin:
            raise RuntimeError(f"{SUBMODULE} has {checked_out} checked out but the gitlink pins {pin}")
    initialize = bool(pin and not os.path.lexists(submodule_path / ".git"))
    moved_from = pin if pin and pin != commit else None
    if moved_from and not initialize:
        changed = git("-C", SUBMODULE, "status", "--porcelain", "--untracked-files=no",
                      cwd=target).stdout.splitlines()
        if changed:
            raise RuntimeError(f"{SUBMODULE} has uncommitted changes, so its pin is not moved: " +
                               ", ".join(line[3:] for line in changed) +
                               "; commit or discard them in the-way and run again")
    return files, shared, stale_entry_points(target), pin is None, initialize, moved_from


def going_back(target: Path, pin: str, commit: str) -> bool:
    """Whether `commit` is older than `pin`, as the-way's history or the checkout's knows it."""
    for cwd in (SOURCE, target / SUBMODULE):
        if not os.path.lexists(cwd / ".git"):
            continue
        found = git("merge-base", "--is-ancestor", commit, pin, cwd=cwd, check=False)
        if found.returncode in (0, 1):
            return found.returncode == 0
    return False


def untracked_in_checkout(target: Path) -> list[str]:
    if not os.path.lexists(target / SUBMODULE / ".git"):
        return []
    listed = git("-C", SUBMODULE, "status", "--porcelain", "--untracked-files=all",
                 cwd=target).stdout.splitlines()
    return [line[3:] for line in listed if line.startswith("?? ")]


def file_action(path: Path, content: str) -> str:
    if not os.path.lexists(path):
        return "CREATE"
    if path.parts[-2] == "foundations" or path.read_bytes() == content.encode("utf-8"):
        return "KEEP"
    return "REPLACE"


def shown_diff(name: str, before: str, after: str) -> str:
    return "\n".join(difflib.unified_diff(before.splitlines(), after.splitlines(),
                                         fromfile=name, tofile=name, lineterm=""))


def ignored_paths(target: Path, paths: list[Path]) -> list[str]:
    """The paths the installer writes that git ignores in the product, so they cannot be
    committed. A tracked path counts as not ignored, since git commits it anyway."""
    names = [path.relative_to(target).as_posix() for path in paths]
    result = git("check-ignore", "-z", "--stdin", cwd=target, check=False,
                 stdin="\0".join(names) + "\0")
    if result.returncode not in (0, 1):
        raise RuntimeError("git cannot tell which paths it ignores: " +
                           (result.stderr.strip() or f"exit code {result.returncode}"))
    ignored = set(result.stdout.split("\0"))
    return [name for name in names if name in ignored]


def warnings_for(target: Path, files: dict[Path, str],
                 shared: dict[Path, tuple[str, str]]) -> list[str]:
    warnings = []
    ignored = ignored_paths(target, [*files, *shared])
    if ignored:
        warnings.append("git ignores these paths in this repository, so they cannot be committed "
                        "and other clones and cloud sessions will not get them: " +
                        ", ".join(ignored))
    if shared[target / CLAUDE][0] == "KEEP" and not has_agents_import(
            read_text_file(target / CLAUDE, CLAUDE)):
        warnings.append(f"{CLAUDE} has no effective @AGENTS.md import; Claude Code may miss "
                        f"the shared instructions in {AGENTS}. Add @AGENTS.md by hand")
    if os.path.lexists(target / CODEX_OVERRIDE):
        warnings.append(f"{CODEX_OVERRIDE} exists; Codex reads it instead of {AGENTS}, so it will "
                        f"not see the the-way block unless {CODEX_OVERRIDE} carries the same text")
    action, text = shared[target / AGENTS]
    size = len(text.encode("utf-8"))
    if action in ("APPEND", "KEEP"):
        # APPEND carries the added lines alone; REPLACE and CREATE carry the whole new file.
        size += (target / AGENTS).stat().st_size
    if size > CODEX_LIMIT:
        warnings.append(f"{AGENTS} will hold {size} bytes; Codex reads at most {CODEX_LIMIT} bytes "
                        "of instructions, so it may not see the whole the-way block")
    return warnings


def run() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="root of the product Git repository")
    parser.add_argument("--url", help="Git URL for the submodule (default: the-way's origin)")
    parser.add_argument("--apply", action="store_true", help="write after showing the plan and confirming")
    args = parser.parse_args()
    target = args.repo.resolve()
    if not target.is_dir():
        raise RuntimeError(f"Not a directory: {target}")
    inside_repo(target)
    commit = git("rev-parse", "--verify", "HEAD^{commit}", cwd=SOURCE).stdout.strip()
    url = args.url or git("remote", "get-url", "origin", cwd=SOURCE).stdout.strip()
    parsed_url = urlsplit(url)
    if parsed_url.password or (parsed_url.username and parsed_url.scheme in ("http", "https")):
        raise RuntimeError("Submodule URL contains credentials; use a credential-free URL")
    if is_local(url):
        FILE_PROTOCOL[:] = ["-c", "protocol.file.allow=always"]
    files, shared, stale, add_submodule, initialize_submodule, moved_from = \
        plan(target, commit, url)

    print(f"Product: {target}\nProcess commit: {commit}\nSubmodule URL: {url}")
    if moved_from:
        older = " (older than the pin)" if going_back(target, moved_from, commit) else ""
        print(f"MOVE {SUBMODULE} from {moved_from} to {commit}{older} (checks it out and stages "
              "the gitlink)")
    else:
        print(f"{'ADD' if add_submodule else 'KEEP'} {SUBMODULE} (gitlink at {commit})")
    if add_submodule:
        print(f"UPDATE .gitmodules: add path={SUBMODULE}, url={url}")
        print(f"+[submodule \"{SUBMODULE}\"]\n+\tpath = {SUBMODULE}\n+\turl = {url}")
        print("STAGE .gitmodules and .the-way (git submodule add stages these paths)")
    if initialize_submodule:
        print(f"INITIALIZE {SUBMODULE} from its pinned commit")
    actions = {path: file_action(path, content) for path, content in files.items()}
    for path, content in files.items():
        name = path.relative_to(target).as_posix()
        print(f"{actions[path]} {name}")
        if actions[path] == "CREATE":
            print("\n".join(difflib.unified_diff([], content.splitlines(), fromfile="/dev/null",
                                                 tofile=name, lineterm="")))
        elif actions[path] == "REPLACE":
            print(shown_diff(name, path.read_bytes().decode("utf-8"), content))
    for path in stale:
        print(f"DELETE {path.relative_to(target).as_posix()} (its skill is no longer in the-way)")
    for path, (action, text) in shared.items():
        name = path.relative_to(target).as_posix()
        print(f"{action} {name}")
        if action == "CREATE":
            print("\n".join(difflib.unified_diff([], text.splitlines(), fromfile="/dev/null",
                                                 tofile=name, lineterm="")))
        elif action == "APPEND":
            print("(added at the end; the existing content stays byte for byte)")
            shown = text.replace("\r\n", "\n")
            existing = path.read_bytes()
            if existing and not existing.endswith(b"\n"):
                shown = shown[1:]   # this newline only ends the existing last line
            print("\n".join("+" + line for line in shown.split("\n")[:-1]))
        elif action == "REPLACE":
            print("(the block is rewritten where it stands; the rest stays byte for byte)")
            print(shown_diff(name, read_text_file(path, name).replace("\r\n", "\n"),
                             text.replace("\r\n", "\n")))
    warnings = warnings_for(target, files, shared)
    untracked = untracked_in_checkout(target) if moved_from else []
    if untracked:
        warnings.append(f"{SUBMODULE} holds files git does not track: {', '.join(untracked)}; "
                        "the move keeps them, and no other clone has them")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if not args.apply:
        print("Preview only. Run again with --apply to confirm and write.")
        return 0
    if not add_submodule and not initialize_submodule and not moved_from and not stale and \
            all(action == "KEEP" for action in actions.values()) and \
            all(action == "KEEP" for action, _ in shared.values()):
        print("Already installed; no changes.")
        return 0
    if input("Apply these changes? [y/N] ").strip().lower() != "y":
        print("Cancelled; no changes.")
        return 0

    if add_submodule or moved_from:
        verify_remote(url, commit)
    if add_submodule:
        git("submodule", "add", "--", url, SUBMODULE, cwd=target)
        if git("-C", SUBMODULE, "cat-file", "-e", f"{commit}^{{commit}}", cwd=target,
               check=False).returncode:
            git("-C", SUBMODULE, "fetch", "--quiet", "origin", commit, cwd=target)
        git("-C", SUBMODULE, "checkout", "--quiet", "--detach", commit, cwd=target)
        git("add", "--", SUBMODULE, cwd=target)
    elif initialize_submodule:
        git("submodule", "update", "--init", "--", SUBMODULE, cwd=target)
    if moved_from:
        if git("-C", SUBMODULE, "cat-file", "-e", f"{commit}^{{commit}}", cwd=target,
               check=False).returncode:
            git("-C", SUBMODULE, "fetch", "--quiet", "origin", commit, cwd=target)
        git("-C", SUBMODULE, "checkout", "--quiet", "--detach", commit, cwd=target)
        git("add", "--", SUBMODULE, cwd=target)
    for path, content in files.items():
        if actions[path] == "CREATE":
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        elif actions[path] == "REPLACE":
            path.write_bytes(content.encode("utf-8"))
    for path in stale:
        path.unlink()
        if not any(path.parent.iterdir()):
            path.parent.rmdir()
    for path, (action, text) in shared.items():
        if action == "CREATE":
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        elif action == "APPEND":
            with path.open("ab") as handle:
                handle.write(text.encode("utf-8"))
        elif action == "REPLACE":
            path.write_bytes(text.encode("utf-8"))
    print("Installed. Commit the product files and gitlink when ready.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        sys.exit(run())
    except (RuntimeError, OSError, EOFError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
