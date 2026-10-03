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
    "critique": "elements/common/critique/SKILL.md",
})
# Claude Code reads project skills from .claude/skills, Codex from .agents/skills.
SKILL_DIRECTORIES = (".claude", ".agents")
RULE = Path(".claude") / "rules" / "the-way.md"
AGENTS = "AGENTS.md"
BEGIN = "<!-- the-way:begin -->"
END = "<!-- the-way:end -->"
IGNORE = ".gitignore"
RUNS = ".runs/"
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
            "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n\n"
            "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|\n\n"
            "## Recovered invariants\n\n| Identifier | Version | Searched | Found |\n|---|---|---|---|\n"
        ),
        "glossary.md": "# Glossary\n\nTerms used by this product's foundation.\n",
        "part_map.md": (
            "# Part map\n\n"
            "## Criticality scale\n\n"
            "## External context\n\n"
            "| Partner | Direction | What comes in | Updates with the product |\n"
            "|---|---|---|---|\n\n"
            "## Change paths\n\n"
            "| Promise level | What a change at this level may do | What it owes the consumer first |\n"
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
    original = committed(path, commit)
    original_name = re.search(r"^name: (.+)$", original, re.M)
    if not original_name or original_name.group(1) != name:
        raise RuntimeError(f"Unexpected skill name for {path} at {commit}")
    description = re.search(r"^description: (.+)$", original, re.M)
    if not description:
        raise RuntimeError(f"Missing skill description for {path}")
    project_name = f"the-way-{name}"
    return (f"---\nname: {project_name}\n"
            f"description: {description.group(1)} Use this product's pinned the-way commit.\n"
            "---\n\n"
            f"# {project_name}\n\n"
            f"The process for this repository is pinned as the Git submodule `{SUBMODULE}`. "
            f"Its commit is `{commit}`.\n\n"
            f"If `{SUBMODULE}/{path}` is absent, run "
            f"`git submodule update --init -- {SUBMODULE}` from the product root. "
            f"Check `git ls-files --stage -- {SUBMODULE}` and "
            f"`git -C {SUBMODULE} rev-parse HEAD`: both must show `{commit}`. "
            "If initialization fails or either commit differs, stop.\n\n"
            f"Read `{SUBMODULE}/{path}` in full and follow it. "
            f"Read the files it references inside `{SUBMODULE}`. "
            "Its paragraph about resolving a global skill link applies only to a global install; "
            f"here the process root is `{SUBMODULE}`. Do not substitute a global skill.\n\n"
            f"Where this skill or a file it reads names another the-way skill — {sibling_names()} "
            "— use this product's project skill of the same name with the `the-way-` prefix, "
            "never an unprefixed one.\n")


def product_guidance() -> str:
    """The guidance for agents in a product. It names no commit: the gitlink records the commit,
    so the text changes only when the guidance itself changes, not when the pin moves."""
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
            "skill, never a personal skill of that name.\n\n"
            "Run the-way's scripts from this repository's root as "
            f"`{SUBMODULE}/<path>` and always name this repository's file or directory, e.g. "
            f"`python -B {SUBMODULE}/gate/run_tests.py <directory>` and "
            f"`python -B {SUBMODULE}/elements/<element>/format_guard.py foundations/<file>`. "
            f"A guard run inside `{SUBMODULE}` without a file checks the-way's own files. "
            f"Records of a run (`--record`) go under `{RUNS}`, which `.gitignore` must keep "
            "ignored.\n\n"
            "The main branch is the branch task branches merge into. In a clone, "
            "`git symbolic-ref --short refs/remotes/origin/HEAD` names it as `origin/<branch>`; "
            "otherwise ask the human. On a task branch pass `--base` the commit "
            "`git merge-base HEAD <main branch>` prints and `--merge-onto` the commit of the main "
            "branch the merge goes onto (the part map's guard takes no `--merge-onto`). Pass "
            "`none` only while this repository has no main branch at all; a command that cannot "
            "find the branch means a wrong name, not a missing branch. With `none` the checks that "
            "need the commit stay unchecked.\n\n"
            "Until the part map has its first parts, its guard reports every tracked file as "
            "claimed by no part; that is expected, and it is not a pass.\n\n"
            "Nothing runs these checks automatically. Before a merge, run the format guard of "
            "every changed foundation file and the tests of every changed part, and report what "
            "failed and what stayed unchecked. A check that did not run is never a pass.\n")


def agents_block() -> str:
    return f"{BEGIN}\n{product_guidance()}{END}\n"


def read_text_file(path: Path, name: str) -> str:
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"Existing {name} is not a regular file")
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as error:
        raise RuntimeError(f"Existing {name} is not UTF-8 text") from error


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
    """CREATE, APPEND or KEEP the marked block of the product guidance in AGENTS.md."""
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
        raise RuntimeError(f"{AGENTS} holds a the-way block that differs from this commit's "
                           f"guidance; remove the block from {BEGIN} to {END} and run again")
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


def plan(target: Path, commit: str,
         url: str) -> tuple[dict[Path, str], dict[Path, tuple[str, str]], bool, bool]:
    files: dict[Path, str] = {}
    for filename, content in empty_foundations().items():
        files[target / "foundations" / filename] = content
    for name, path in SKILLS.items():
        wrapper = skill_wrapper(path, name, commit)
        for directory in SKILL_DIRECTORIES:
            files[target / directory / "skills" / f"the-way-{name}" / "SKILL.md"] = wrapper
    files[target / RULE] = product_guidance()
    shared = {target / AGENTS: agents_change(target / AGENTS),
              target / IGNORE: ignore_change(target / IGNORE)}

    pin = existing_pin(target)
    submodule_path = target / SUBMODULE
    modules_file = target / ".gitmodules"
    if pin:
        if pin != commit:
            raise RuntimeError(f"Existing {SUBMODULE} pins {pin}, requested {commit}; "
                               "moving a pin is a separate product task")
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
        elif not path.is_file() or path.is_symlink() or path.read_text(encoding="utf-8") != expected:
            raise RuntimeError(f"Existing integration file differs: {path}")
    if pin and os.path.lexists(submodule_path / ".git"):
        checked_out = git("-C", SUBMODULE, "rev-parse", "HEAD", cwd=target).stdout.strip()
        if checked_out != pin:
            raise RuntimeError(f"{SUBMODULE} has {checked_out} checked out but the gitlink pins {pin}")
    return files, shared, pin is None, bool(pin and not os.path.lexists(submodule_path / ".git"))


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
    if os.path.lexists(target / CODEX_OVERRIDE):
        warnings.append(f"{CODEX_OVERRIDE} exists; Codex reads it instead of {AGENTS}, so it will "
                        f"not see the the-way block unless {CODEX_OVERRIDE} carries the same text")
    action, text = shared[target / AGENTS]
    size = len(text.encode("utf-8"))
    if action != "CREATE":
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
    files, shared, add_submodule, initialize_submodule = plan(target, commit, url)

    print(f"Product: {target}\nProcess commit: {commit}\nSubmodule URL: {url}")
    print(f"{'ADD' if add_submodule else 'KEEP'} {SUBMODULE} (gitlink at {commit})")
    if add_submodule:
        print(f"UPDATE .gitmodules: add path={SUBMODULE}, url={url}")
        print(f"+[submodule \"{SUBMODULE}\"]\n+\tpath = {SUBMODULE}\n+\turl = {url}")
        print("STAGE .gitmodules and .the-way (git submodule add stages these paths)")
    elif initialize_submodule:
        print(f"INITIALIZE {SUBMODULE} from its pinned commit")
    for path, content in files.items():
        action = "KEEP" if os.path.lexists(path) else "CREATE"
        print(f"{action} {path.relative_to(target).as_posix()}")
        if action == "CREATE":
            print("\n".join(difflib.unified_diff([], content.splitlines(), fromfile="/dev/null",
                                                 tofile=path.relative_to(target).as_posix(),
                                                 lineterm="")))
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
    for warning in warnings_for(target, files, shared):
        print(f"WARNING: {warning}")
    if not args.apply:
        print("Preview only. Run again with --apply to confirm and write.")
        return 0
    if not add_submodule and not initialize_submodule and \
            all(os.path.lexists(path) for path in files) and \
            all(action == "KEEP" for action, _ in shared.values()):
        print("Already installed; no changes.")
        return 0
    if input("Apply these changes? [y/N] ").strip().lower() != "y":
        print("Cancelled; no changes.")
        return 0

    if add_submodule:
        verify_remote(url, commit)
        git("submodule", "add", "--", url, SUBMODULE, cwd=target)
        if git("-C", SUBMODULE, "cat-file", "-e", f"{commit}^{{commit}}", cwd=target,
               check=False).returncode:
            git("-C", SUBMODULE, "fetch", "--quiet", "origin", commit, cwd=target)
        git("-C", SUBMODULE, "checkout", "--quiet", "--detach", commit, cwd=target)
        git("add", "--", SUBMODULE, cwd=target)
    elif initialize_submodule:
        git("submodule", "update", "--init", "--", SUBMODULE, cwd=target)
    for path, content in files.items():
        if os.path.lexists(path):
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    for path, (action, text) in shared.items():
        if action == "CREATE":
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        elif action == "APPEND":
            with path.open("ab") as handle:
                handle.write(text.encode("utf-8"))
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
