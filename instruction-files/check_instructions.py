"""Mechanical checks of a repository's instruction files for agents.

Settles, without reading what the rules say, the checks of section 6 of principles.md, which lies
next to this script: paths that do not exist, `@path` imports that Claude Code loads into every
session or silently skips, Cursor rules that Cursor ignores, a root layout that hides `AGENTS.md`
from Claude Code, subdirectory `AGENTS.md` files Codex will not reach, skills one of the tools
cannot discover, emphasis spread over several rules, and the size of every file.

Usage, from anywhere:

    python -B <the-way>/instruction-files/check_instructions.py [ROOT] [--file PATH ...]

ROOT defaults to the current directory. --file adds an instruction file outside the repository,
such as the user's global file. Each finding is printed as `LEVEL check file:line message`; the
last line counts the findings by level. The exit code is 1 when there is an error, 2 when ROOT is
not a directory or a --file is not a readable regular file, else 0.

The files it reads are not the-way's, so it trusts none of them: it reads at most 1048576 bytes of
a file, opens only regular files, reads no file through a link that leads out of ROOT, follows no
link to a directory, and prints every value escaped and cut to 200 characters. It writes nothing
and starts no program.
"""

import argparse
import codecs
import os
import re
import stat
import sys
from dataclasses import dataclass

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".runs"}
MAIN_NAMES = {"AGENTS.md", "CLAUDE.md", "CLAUDE.local.md", "AGENTS.override.md"}
SKILL_DIRS = (".claude/skills", ".agents/skills", ".cursor/skills", ".codex/skills")
MAX_BYTES = 1048576
MAX_SHOWN = 200
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
BOMS_NOT_UTF8 = (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE, codecs.BOM_UTF16_LE,
                 codecs.BOM_UTF16_BE)


@dataclass(frozen=True)
class Finding:
    level: str  # error, warn or info
    check: str
    file: str
    line: int
    message: str


def shown(value):
    """VALUE as it may be printed: control and bidirectional-format characters escaped, and cut
    to MAX_SHOWN characters, the last of them `…`."""
    out = []
    for character in str(value):
        code = ord(character)
        if code < 0x20 or 0x7F <= code <= 0x9F:
            out.append("\\x%02x" % code)
        elif 0x202A <= code <= 0x202E or 0x2066 <= code <= 0x2069:
            out.append("\\u%04x" % code)
        else:
            out.append(character)
    text = "".join(out)
    return text if len(text) <= MAX_SHOWN else text[:MAX_SHOWN - 1] + "…"


def reason(error):
    """The reason an OSError gives, without the path it names."""
    return error.strerror or type(error).__name__


def inside(path, directory):
    """True when the real PATH lies in the real DIRECTORY or is it."""
    try:
        common = os.path.commonpath([path, directory])
    except ValueError:
        return False
    return os.path.normcase(common) == os.path.normcase(directory)


def is_instruction_name(rel, name):
    if name in MAIN_NAMES or rel.endswith(".claude/CLAUDE.md"):
        return True
    if "/.claude/rules/" in "/" + rel and name.endswith(".md"):
        return True
    if "/.cursor/rules/" in "/" + rel:
        return True
    return name == "SKILL.md" and any(("/" + d + "/") in "/" + rel for d in SKILL_DIRS)


def instruction_files(root, findings):
    """Every file under ROOT that an agent tool reads as instructions, as paths relative to ROOT.
    A link to a directory is not followed, a file reached through a link that leads out of ROOT
    is not listed, and a directory that cannot be listed is reported."""
    real_root = os.path.realpath(root)
    found = []

    def relative(path):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        return "" if rel == "." else rel

    def cannot_list(error):
        findings.append(Finding("info", "walk", relative(error.filename or root) or ".", 0,
                                f"a directory that cannot be listed: {reason(error)}"))

    for current, dirs, files in os.walk(root, onerror=cannot_list):
        rel_dir = relative(current)
        rel_dir = rel_dir + "/" if rel_dir else ""
        kept = []
        for name in sorted(dirs):
            full = os.path.join(current, name)
            if name in SKIP_DIRS:
                continue
            if os.path.islink(full) or os.path.isjunction(full):
                findings.append(Finding("info", "walk", rel_dir + name, 0,
                                        "a link to a directory, not followed"))
                continue
            if os.path.exists(os.path.join(full, ".git")):
                continue
            if name in MAIN_NAMES:
                findings.append(Finding("warn", "read", rel_dir + name, 0,
                                        "cannot be read: it is a directory"))
            kept.append(name)
        dirs[:] = kept
        for name in sorted(files):
            rel = rel_dir + name
            if not is_instruction_name(rel, name):
                continue
            full = os.path.join(current, name)
            if os.path.islink(full) and not inside(os.path.realpath(full), real_root):
                findings.append(Finding("info", "read", rel, 0,
                                        "a link out of the repository, not read"))
                continue
            found.append(rel)
    return found


def read_text(path, shown_as, findings):
    """The text of the regular file at PATH, its UTF-8 byte order mark removed, or None when it
    cannot be read or is no UTF-8 text; what stopped it is reported as a finding."""
    try:
        mode = os.stat(path).st_mode
    except OSError as error:
        findings.append(Finding("warn", "read", shown_as, 0, f"cannot be read: {reason(error)}"))
        return None
    if stat.S_ISDIR(mode):
        findings.append(Finding("warn", "read", shown_as, 0, "cannot be read: it is a directory"))
        return None
    if not stat.S_ISREG(mode):
        findings.append(Finding("warn", "read", shown_as, 0,
                                "cannot be read: it is not a regular file"))
        return None
    try:
        with open(path, "rb") as handle:
            data = handle.read(MAX_BYTES + 1)
    except OSError as error:
        findings.append(Finding("warn", "read", shown_as, 0, f"cannot be read: {reason(error)}"))
        return None
    cut = len(data) > MAX_BYTES
    if cut:
        data = data[:MAX_BYTES]
        findings.append(Finding("info", "read", shown_as, 0,
                                f"only the first {MAX_BYTES} bytes were checked"))
    if data.startswith(BOMS_NOT_UTF8):
        findings.append(Finding("warn", "read", shown_as, 0,
                                "not UTF-8 text; its content was not checked"))
        return None
    if data.startswith(codecs.BOM_UTF8):
        data = data[len(codecs.BOM_UTF8):]
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as error:
        if cut and error.start >= len(data) - 3:
            return data[:error.start].decode("utf-8")
        findings.append(Finding("warn", "read", shown_as, 0,
                                "not UTF-8 text; its content was not checked"))
        return None


def prose_lines(text):
    """(line number, line) for every line outside fenced code blocks."""
    inside_fence = False
    for number, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside_fence = not inside_fence
            continue
        if not inside_fence:
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


def is_relative(token):
    return not (token.startswith(("~", "/", "\\")) or re.match(r"^[A-Za-z]:", token))


def resolve(token, file_dir, root):
    token = os.path.expanduser(LINE_SUFFIX.sub("", token).rstrip("/\\"))
    if os.path.isabs(token) or re.match(r"^[A-Za-z]:", token):
        return os.path.exists(token)
    return any(os.path.exists(os.path.join(base, token)) for base in (file_dir, root) if base)


def check_file(path, shown_as, root, findings, in_repo=True):
    """The per-file checks of one instruction file; returns its text, or None when it was not
    read."""
    text = read_text(path, shown_as, findings)
    if text is None:
        return None
    name = os.path.basename(path)
    file_dir = os.path.dirname(path)
    emphasised = []
    for number, line in prose_lines(text):
        for span in CODE_SPAN.findall(line):
            token = span.strip()
            if looks_like_path(token) and not resolve(token, file_dir, root):
                if not in_repo and is_relative(token):
                    findings.append(Finding(
                        "info", "dead-path", shown_as, number,
                        f"`{shown(token)}` is relative in a file outside the repository and does "
                        "not resolve from here"))
                else:
                    findings.append(Finding("warn", "dead-path", shown_as, number,
                                            f"`{shown(token)}` does not exist"))
        bare = CODE_SPAN.sub("", line)
        for match in AT_IMPORT.finditer(bare):
            token = match.group(1)
            if line.strip() == "@AGENTS.md" and name == "CLAUDE.md":
                continue
            if not ("." in token or "/" in token):
                continue
            if token[-1] in TRAILING:
                findings.append(Finding(
                    "error", "at-import", shown_as, number,
                    f"@{shown(token)} — a punctuation mark right after the path stops Claude Code "
                    "from loading it, without a warning"))
            else:
                findings.append(Finding(
                    "warn", "at-import", shown_as, number,
                    f"@{shown(token)} — Claude Code loads the whole file into every session; Codex "
                    "reads it as plain text; a pointer is a path in backticks"))
        if EMPHASIS.search(line):
            emphasised.append(number)
    if len(emphasised) > 1:
        findings.append(Finding("warn", "emphasis", shown_as, emphasised[0],
                                f"{len(emphasised)} emphasised lines — emphasis on one rule at most"))
    if name != "SKILL.md":
        findings.append(Finding("info", "size", shown_as, 0,
                                f"{len(text.splitlines())} lines, {len(text.split())} words"))
    return text


def check_cursor_rule(rel, text, findings):
    if not rel.endswith(".mdc"):
        findings.append(Finding("error", "cursor-rule", rel, 0,
                                "Cursor reads only .mdc files in .cursor/rules; this one is ignored"))
        return
    if text is None:
        return
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        findings.append(Finding("error", "cursor-rule", rel, 1,
                                "a Cursor rule without a YAML header is never attached"))


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
    main = texts.get("AGENTS.md") or ""
    for rel in files:
        if rel != "AGENTS.md" and rel.endswith("/AGENTS.md") and rel not in main:
            findings.append(Finding(
                "warn", "nested-pointer", rel, 0,
                f"no line of the root AGENTS.md points to {shown(rel)}; Codex reads it only when a "
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
    files = instruction_files(root, findings)
    texts = {}
    seen = set()
    for rel in files:
        path = os.path.join(root, *rel.split("/"))
        seen.add(os.path.realpath(path))
        texts[rel] = check_file(path, rel, root, findings)
        if rel.startswith(".cursor/rules/") or "/.cursor/rules/" in rel:
            check_cursor_rule(rel, texts[rel], findings)
    for path in extra:
        if os.path.realpath(path) in seen:
            continue
        check_file(path, path, root, findings, in_repo=False)
    check_layout(root, files, texts, findings)
    return findings


def usage_error(message):
    print(f"Error: {shown(message)}", file=sys.stderr)
    return 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", nargs="?", default=None,
                        help="the repository; defaults to the current directory unless --file is given")
    parser.add_argument("--file", action="append", default=[],
                        help="an instruction file outside the repository")
    args = parser.parse_args(argv)
    root = args.root or (None if args.file else ".")
    if root is not None and not os.path.isdir(root):
        return usage_error(f"ROOT is not a directory: {root}")
    for path in args.file:
        try:
            if not stat.S_ISREG(os.stat(path).st_mode):
                return usage_error(f"--file is not a regular file: {path}")
            with open(path, "rb"):
                pass
        except OSError as error:
            return usage_error(f"--file cannot be read: {path}: {reason(error)}")
    findings = check(root, args.file)
    order = {"error": 0, "warn": 1, "info": 2}
    for f in sorted(findings, key=lambda f: (order[f.level], f.file, f.line)):
        print(f"{f.level.upper():5} {f.check} {shown(f.file)}:{f.line} {f.message}")
    counts = {level: sum(1 for f in findings if f.level == level) for level in order}
    print(f"{counts['error']} error, {counts['warn']} warn, {counts['info']} info")
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
