"""Mechanical checks of a repository's instruction files for agents.

Settles, without reading what the rules say, the checks of section 6 of principles.md, which lies
next to this script: paths that do not exist, `@path` imports that Claude Code loads into every
session or silently skips, Cursor rules that Cursor ignores, a root layout that hides `AGENTS.md`
from Claude Code, subdirectory `AGENTS.md` files Codex will not reach, skills one of the tools
cannot discover, emphasis spread over several rules, and the size of every file.

Usage, from anywhere:

    python <the-way>/instruction-files/check_instructions.py [ROOT] [--file PATH ...]

ROOT defaults to the current directory. --file adds an instruction file outside the repository,
such as the user's global file. Each finding is printed as `LEVEL check file:line message`; the
last line counts the findings by level. The exit code is 1 when there is an error, else 0.
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".runs"}
MAIN_NAMES = {"AGENTS.md", "CLAUDE.md", "CLAUDE.local.md", "AGENTS.override.md"}
SKILL_DIRS = (".claude/skills", ".agents/skills", ".cursor/skills", ".codex/skills")
EMPHASIS = re.compile(r"\b(IMPORTANT|YOU MUST|CRITICAL|MUST NOT|NEVER EVER)\b")
FENCE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN = re.compile(r"`([^`\n]+)`")
AT_IMPORT = re.compile(r"(?<![\w.@/\\])@([^\s`<>\"']+)")
TRAILING = ".,;:)!?]}"
EXTENSIONS = ("md", "mdc", "json", "jsonl", "js", "mjs", "cjs", "ts", "tsx", "jsx", "py", "toml",
              "yaml", "yml", "txt", "sh", "ps1", "bat", "cmd", "sql", "html", "css", "vue", "php",
              "go", "rs", "java", "kt", "rb", "lock", "ini", "cfg", "env", "xml", "csv")
FILE_LIKE = re.compile(r"\.(" + "|".join(EXTENSIONS) + r")$", re.IGNORECASE)
LINE_SUFFIX = re.compile(r":\d+(:\d+)?$")


@dataclass(frozen=True)
class Finding:
    level: str  # error, warn or info
    check: str
    file: str
    line: int
    message: str


def instruction_files(root):
    """Every file under ROOT that an agent tool reads as instructions, as paths relative to ROOT."""
    found = []
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS
                         and not os.path.exists(os.path.join(current, d, ".git")))
        rel_dir = os.path.relpath(current, root).replace(os.sep, "/")
        rel_dir = "" if rel_dir == "." else rel_dir + "/"
        for name in sorted(files):
            rel = rel_dir + name
            if name in MAIN_NAMES or rel.endswith(".claude/CLAUDE.md"):
                found.append(rel)
            elif "/.claude/rules/" in "/" + rel and name.endswith(".md"):
                found.append(rel)
            elif "/.cursor/rules/" in "/" + rel:
                found.append(rel)
            elif name == "SKILL.md" and any(("/" + d + "/") in "/" + rel for d in SKILL_DIRS):
                found.append(rel)
    return found


def prose_lines(text):
    """(line number, line) for every line outside fenced code blocks."""
    inside = False
    for number, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            yield number, line


def looks_like_path(token):
    if not token or token.startswith(("-", "http://", "https://", "$")):
        return False
    if any(c in token for c in "*<>{}|$…") or token.endswith("()"):
        return False
    if token.startswith("/") and "/" not in token[1:] and "." not in token:
        return False  # a slash command such as /park
    first = re.split(r"[\\/]", token)[0]
    if "." in first and not first.startswith(".") and not FILE_LIKE.search(first):
        return False  # a domain such as github.com/someone
    if re.match(r"^[A-Za-z]:[\\/]", token) or token.startswith("~"):
        return True
    if " " in token:
        return False
    return "/" in token or "\\" in token or bool(FILE_LIKE.search(token))


def resolve(token, file_dir, root):
    token = os.path.expanduser(LINE_SUFFIX.sub("", token).rstrip("/\\"))
    if os.path.isabs(token) or re.match(r"^[A-Za-z]:", token):
        return os.path.exists(token)
    return any(os.path.exists(os.path.join(base, token)) for base in (file_dir, root) if base)


def is_relative(token):
    return not (token.startswith(("~", "/", "\\")) or re.match(r"^[A-Za-z]:", token))


def check_file(path, shown, root, findings, in_repo=True):
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    name = os.path.basename(path)
    file_dir = os.path.dirname(path)
    emphasised = []
    for number, line in prose_lines(text):
        for span in CODE_SPAN.findall(line):
            token = span.strip()
            if looks_like_path(token) and not resolve(token, file_dir, root):
                if not in_repo and is_relative(token):
                    findings.append(Finding(
                        "info", "dead-path", shown, number,
                        f"`{token}` is relative in a file outside the repository and does not "
                        "resolve from here"))
                else:
                    findings.append(Finding("warn", "dead-path", shown, number,
                                            f"`{token}` does not exist"))
        bare = CODE_SPAN.sub("", line)
        for match in AT_IMPORT.finditer(bare):
            token = match.group(1)
            if line.strip() == "@AGENTS.md" and name == "CLAUDE.md":
                continue
            if not ("." in token or "/" in token):
                continue
            if token[-1] in TRAILING:
                findings.append(Finding(
                    "error", "at-import", shown, number,
                    f"@{token} — a punctuation mark right after the path stops Claude Code from "
                    "loading it, without a warning"))
            else:
                findings.append(Finding(
                    "warn", "at-import", shown, number,
                    f"@{token} — Claude Code loads the whole file into every session; Codex reads "
                    "it as plain text; a pointer is a path in backticks"))
        if EMPHASIS.search(line):
            emphasised.append(number)
    if len(emphasised) > 1:
        findings.append(Finding("warn", "emphasis", shown, emphasised[0],
                                f"{len(emphasised)} emphasised lines — emphasis on one rule at most"))
    if name != "SKILL.md":
        findings.append(Finding("info", "size", shown, 0,
                                f"{len(text.splitlines())} lines, {len(text.split())} words"))
    return text


def check_layout(root, files, texts, findings):
    present = set(files)
    if "AGENTS.md" in present:
        claude = texts.get("CLAUDE.md")
        if claude is not None and "@AGENTS.md" not in [l.strip() for l in claude.splitlines()]:
            findings.append(Finding(
                "warn", "root-layout", "CLAUDE.md", 0,
                "CLAUDE.md stands beside AGENTS.md without an `@AGENTS.md` line, so Claude Code "
                "does not read AGENTS.md"))
        if "CLAUDE.local.md" in present:
            findings.append(Finding("warn", "root-layout", "CLAUDE.local.md", 0,
                                    "CLAUDE.local.md stops Claude Code from reading AGENTS.md"))
    main = texts.get("AGENTS.md", "")
    for rel in files:
        if rel != "AGENTS.md" and rel.endswith("/AGENTS.md") and rel not in main:
            findings.append(Finding(
                "warn", "nested-pointer", rel, 0,
                f"no line of the root AGENTS.md points to {rel}; Codex reads it only when a "
                "session starts in its directory"))
    unpointed = []
    for rel in files:
        if not rel.endswith("/SKILL.md"):
            continue
        skill_dir = rel[: -len("/SKILL.md")]
        if rel.startswith(".agents/skills/") or "/.agents/skills/" in rel:
            twin = skill_dir.replace(".agents/skills", ".claude/skills") + "/SKILL.md"
            if twin not in present:
                findings.append(Finding("warn", "skill-dir", rel, 0,
                                        "Claude Code does not read .agents/skills"))
        elif rel.startswith(".claude/skills/") and skill_dir not in main:
            unpointed.append(skill_dir)
    if unpointed:
        findings.append(Finding(
            "info", "skill-dir", ".claude/skills", 0,
            f"{len(unpointed)} skills in .claude/skills have no pointer in AGENTS.md; Codex does "
            "not read .claude/skills, so point to the SKILL.md of each one Codex needs"))


def check(root, extra=()):
    """Findings for the instruction files of the repository at ROOT and for EXTRA files. With ROOT
    None, only the EXTRA files are checked."""
    findings = []
    if root is None:
        for path in extra:
            check_file(path, path, None, findings, in_repo=False)
        return findings
    root = os.path.abspath(root)
    files = instruction_files(root)
    texts = {}
    seen = set()
    for rel in files:
        path = os.path.join(root, *rel.split("/"))
        seen.add(os.path.realpath(path))
        if rel.startswith(".cursor/rules/") or "/.cursor/rules/" in rel:
            check_cursor_rule(path, rel, findings)
        texts[rel] = check_file(path, rel, root, findings)
    for path in extra:
        if os.path.realpath(path) in seen:
            continue
        check_file(path, path, root, findings, in_repo=False)
    check_layout(root, files, texts, findings)
    return findings


def check_cursor_rule(path, rel, findings):
    if not rel.endswith(".mdc"):
        findings.append(Finding("error", "cursor-rule", rel, 0,
                                "Cursor reads only .mdc files in .cursor/rules; this one is ignored"))
        return
    with open(path, encoding="utf-8", errors="replace") as handle:
        first = handle.readline().strip()
    if first != "---":
        findings.append(Finding("error", "cursor-rule", rel, 1,
                                "a Cursor rule without a YAML header is never attached"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", nargs="?", default=None,
                        help="the repository; defaults to the current directory unless --file is given")
    parser.add_argument("--file", action="append", default=[],
                        help="an instruction file outside the repository")
    args = parser.parse_args(argv)
    root = args.root or (None if args.file else ".")
    findings = check(root, args.file)
    order = {"error": 0, "warn": 1, "info": 2}
    for f in sorted(findings, key=lambda f: (order[f.level], f.file, f.line)):
        print(f"{f.level.upper():5} {f.check} {f.file}:{f.line} {f.message}")
    counts = {level: sum(1 for f in findings if f.level == level) for level in order}
    print(f"{counts['error']} error, {counts['warn']} warn, {counts['info']} info")
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
