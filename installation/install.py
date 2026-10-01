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


# Set by run() only when the submodule URL is a local path or a file:// URL.
FILE_PROTOCOL: list[str] = []


def is_local(url: str) -> bool:
    return url.startswith("file://") or Path(url).exists()


def git(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(["git", *FILE_PROTOCOL, *args], cwd=cwd,
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


def skill_wrapper(element: str, name: str, commit: str) -> str:
    original = committed(f"elements/{element}/skill/SKILL.md", commit)
    original_name = re.search(r"^name: (.+)$", original, re.M)
    if not original_name or original_name.group(1) != name:
        raise RuntimeError(f"Unexpected skill name for {element} at {commit}")
    description = re.search(r"^description: (.+)$", original, re.M)
    if not description:
        raise RuntimeError(f"Missing skill description for {element}")
    project_name = f"the-way-{name}"
    return (f"---\nname: {project_name}\n"
            f"description: {description.group(1)} Use this product's pinned the-way commit.\n"
            "---\n\n"
            f"# {project_name}\n\n"
            f"The process for this repository is pinned as the Git submodule `{SUBMODULE}`. "
            f"Its commit is `{commit}`.\n\n"
            f"If `{SUBMODULE}/elements/{element}/skill/SKILL.md` is absent, run "
            f"`git submodule update --init -- {SUBMODULE}` from the product root. "
            f"Check `git ls-files --stage -- {SUBMODULE}` and "
            f"`git -C {SUBMODULE} rev-parse HEAD`: both must show `{commit}`. "
            "If initialization fails or either commit differs, stop.\n\n"
            f"Read `{SUBMODULE}/elements/{element}/skill/SKILL.md` in full and follow it. "
            f"Read its referenced template and `elements/common/` files inside `{SUBMODULE}`. "
            "Its paragraph about resolving a global skill link applies only to a global install; "
            f"here the process root is `{SUBMODULE}`. Do not substitute a global skill.\n")


def project_rule(commit: str) -> str:
    names = ", ".join(f"`/the-way-{name}`" for name, _ in ELEMENTS.values())
    return ("# Pinned the-way process\n\n"
            f"This repository uses the-way at commit `{commit}` through the `{SUBMODULE}` "
            "Git submodule. Initialize it after a fresh clone with "
            f"`git submodule update --init -- {SUBMODULE}`. Check that "
            f"`git -C {SUBMODULE} rev-parse HEAD` matches the gitlink commit before using it.\n\n"
            f"For foundation entries, use the project skills {names}. "
            "They read the pinned submodule. Personal skills with similar unprefixed names may "
            "use another version of the process. If the submodule cannot be initialized, stop "
            "rather than using a different version.\n")


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


def plan(target: Path, commit: str, url: str) -> tuple[dict[Path, str], bool, bool]:
    files: dict[Path, str] = {}
    for filename, content in empty_foundations().items():
        files[target / "foundations" / filename] = content
    for element, (name, _) in ELEMENTS.items():
        files[target / ".claude" / "skills" / f"the-way-{name}" / "SKILL.md"] = \
            skill_wrapper(element, name, commit)
    files[target / ".claude" / "rules" / "the-way.md"] = project_rule(commit)

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
    return files, pin is None, bool(pin and not os.path.lexists(submodule_path / ".git"))


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
    files, add_submodule, initialize_submodule = plan(target, commit, url)

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
    if not args.apply:
        print("Preview only. Run again with --apply to confirm and write.")
        return 0
    if not add_submodule and not initialize_submodule and \
            all(os.path.lexists(path) for path in files):
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
