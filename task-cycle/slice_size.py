"""The size of each slice of a task's plan — how much its agent has to read and how many files it
changes — and which slices are too large for one agent (WAY-136). It measures a plan after the
cycle selects planning; it does not decide whether a change fits the one-author route. That
judgment comes from the task document, also after a reviewed spec, without a preliminary plan.

Usage:

    python -B task-cycle/slice_size.py PLAN [--root DIR]

PLAN is a plan in the form `task-cycle/plan/SKILL.md` gives: each slice under a heading
`### Slice <id> — <goal>`, with a field `- **Change:**` naming the files the slice changes or
creates and a field `- **Read:**` naming the files its agent reads, each path in backticks, the
fields' lines continued on lines indented below them, and `none` for an empty field. A path in
*Read* may end in `:<first>-<last>` to count only those lines of the file. Paths are relative to
DIR, the repository the plan is for, which defaults to the current directory. A path of *Change*
that names nothing under DIR is a file the slice creates, with nothing to read.

A slice reads every file of *Read* and every file of *Change* that exists, each counted once: a
whole file where either field names it whole, otherwise the lines its ranges name. Its size to read
is the number of characters of that text, and its tokens are estimated from them as the source
below gives, never counted by a tokenizer: the estimate is rough, and how many steps an agent takes
is not in it. A slice is too large when its estimated tokens exceed READ_LIMIT_TOKENS or it changes
more than CHANGE_LIMIT files. A slice with neither field, a path that leaves DIR or names something
other than a file there — in *Read*, anything but an existing file — a range in *Change*, or a
range beyond its file leaves the slice unchecked: its size is not known.

The limits start with a wide margin and are corrected as cycles bring data:

- CONTEXT_WINDOW_TOKENS and CHARACTERS_PER_TOKEN come from
  https://platform.claude.com/docs/en/about-claude/models/overview.md, read on 2026-10-10: its
  table "Compare models" gives "1M tokens" as the context window of Claude Fable 5.1, Claude Opus
  5.5, Claude Sonnet 5.5 and Claude Haiku 5.5, and its note on the context window says "1M tokens
  is roughly 555k words or 2.5M Unicode characters on the current tokenizer".
- READ_LIMIT_TOKENS is a quarter of that window, which leaves three quarters for what the agent
  reads again, the output of the commands it runs, and what it writes.
- CHANGE_LIMIT is a starting value with no source.

The report is Markdown, printed: a row for each slice with the files it changes, the characters
and estimated tokens it reads, its verdict — `fits`, `too large` or `unchecked` — and why. Exit
code: 0 when every slice fits; 1 when a slice is too large or unchecked; 2 with `Error: <message>`
on stderr when the plan cannot be read, holds no slice, names two slices alike, or holds a heading
`### Slice` in another form.

Standard library only.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

CONTEXT_WINDOW_TOKENS = 1_000_000
CHARACTERS_PER_TOKEN = 2.5
READ_LIMIT_TOKENS = CONTEXT_WINDOW_TOKENS // 4
CHANGE_LIMIT = 10

SLICE_HEADING = re.compile(r"### Slice (\S+?)(?:\s+—.*)?\s*")
SLICE_START = re.compile(r"###\s+Slice\b")
FIELD = re.compile(r"- \*\*(Change|Read):\*\*(.*)")
OTHER_FIELD = re.compile(r"- \*\*[^*]+:\*\*")
PATH = re.compile(r"`([^`]+)`")
RANGE = re.compile(r"(.+):(\d+)-(\d+)")


class SliceSizeError(Exception):
    """The plan cannot be read as a plan."""


@dataclass
class Slice:
    ident: str
    change: list[str] = field(default_factory=list)
    read: list[str] = field(default_factory=list)
    fields: set[str] = field(default_factory=set)


@dataclass
class Size:
    ident: str
    changed: int
    characters: int | None
    problems: list[str]

    @property
    def tokens(self) -> int | None:
        if self.characters is None:
            return None
        return math.ceil(self.characters / CHARACTERS_PER_TOKEN)

    @property
    def verdict(self) -> tuple[str, list[str]]:
        reasons = []
        if self.changed > CHANGE_LIMIT:
            reasons.append(f"changes {self.changed} files, more than {CHANGE_LIMIT}")
        if self.tokens is not None and self.tokens > READ_LIMIT_TOKENS:
            reasons.append(f"reads about {self.tokens} tokens, more than {READ_LIMIT_TOKENS}")
        if reasons:
            return "too large", reasons + self.problems
        if self.problems:
            return "unchecked", self.problems
        return "fits", []


def parse_plan(text: str) -> list[Slice]:
    slices: list[Slice] = []
    current: Slice | None = None
    target: list[str] | None = None
    for line in text.splitlines():
        heading = SLICE_HEADING.fullmatch(line)
        if heading:
            current = Slice(heading.group(1))
            slices.append(current)
            target = None
            continue
        if SLICE_START.match(line):
            raise SliceSizeError(f"a slice heading is not `### Slice <id> — <goal>`: {line}")
        if line.startswith("#"):
            current = target = None
            continue
        if current is None:
            continue
        found = FIELD.fullmatch(line)
        if found:
            target = current.change if found.group(1) == "Change" else current.read
            current.fields.add(found.group(1))
            target.extend(paths(found.group(2)))
        elif target is not None and line.startswith("  ") and not OTHER_FIELD.match(line.strip()):
            target.extend(paths(line))
        else:
            target = None
    if not slices:
        raise SliceSizeError("the plan holds no heading `### Slice <id>`")
    seen = set()
    for item in slices:
        if item.ident in seen:
            raise SliceSizeError(f"two slices are named {item.ident}")
        seen.add(item.ident)
    return slices


def paths(text: str) -> list[str]:
    return [path for path in PATH.findall(text) if path != "none"]


def locate(root: Path, written: str) -> Path | None:
    """The file a path of the plan names under the root, or None where it names none there."""
    candidate = (root / written).resolve()
    if not candidate.is_relative_to(root) or not candidate.is_file():
        return None
    return candidate


def measure(item: Slice, root: Path) -> Size:
    problems: list[str] = []
    if not item.fields:
        problems.append("the slice has neither *Change* nor *Read*")
    whole: dict[Path, str] = {}
    ranges: dict[Path, list[tuple[int, int, str]]] = {}
    changed = dict.fromkeys(item.change)
    for written in changed:
        found = locate(root, written)
        if RANGE.fullmatch(written):
            problems.append(f"`{written}` in *Change* names a range, not a file")
        elif found is not None:
            whole[found] = written
        elif (root / written).resolve().is_relative_to(root) and not (root / written).exists():
            continue  # a file the slice creates has nothing to read
        else:
            problems.append(f"`{written}` names no file under the root")
    for written in dict.fromkeys(item.read):
        span = RANGE.fullmatch(written)
        name = span.group(1) if span else written
        found = locate(root, name)
        if found is None:
            problems.append(f"`{written}` names no file under the root")
        elif span:
            first, last = int(span.group(2)), int(span.group(3))
            if first < 1 or last < first:
                problems.append(f"`{written}` names no range of lines")
            else:
                ranges.setdefault(found, []).append((first, last, written))
        else:
            whole[found] = written
    characters = 0
    for path in whole:
        characters += len(path.read_text(encoding="utf-8", errors="replace"))
    for path, spans in ranges.items():
        if path in whole:
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
        counted: set[int] = set()
        for first, last, written in spans:
            if last > len(lines):
                problems.append(f"`{written}` goes beyond the file's {len(lines)} lines")
                continue
            counted.update(range(first - 1, last))
        characters += sum(len(lines[index]) for index in counted)
    return Size(item.ident, len(changed), None if problems else characters, problems)


def report(sizes: list[Size]) -> str:
    lines = [
        "# Slice sizes",
        "",
        f"Too large: more than {READ_LIMIT_TOKENS} estimated tokens to read, a quarter of a "
        f"{CONTEXT_WINDOW_TOKENS}-token context window at {CHARACTERS_PER_TOKEN} characters a "
        f"token, or more than {CHANGE_LIMIT} files to change.",
        "",
        "| Slice | Files to change | Characters to read | Estimated tokens | Verdict | Why |",
        "|---|---|---|---|---|---|",
    ]
    for size in sizes:
        verdict, reasons = size.verdict
        characters = "unknown" if size.characters is None else str(size.characters)
        tokens = "unknown" if size.tokens is None else str(size.tokens)
        lines.append(f"| {size.ident} | {size.changed} | {characters} | {tokens} | {verdict} | "
                     f"{'; '.join(reasons) or '—'} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("plan", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        try:
            text = args.plan.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            raise SliceSizeError(f"cannot read {args.plan}: {error}") from error
        root = args.root.resolve()
        if not root.is_dir():
            raise SliceSizeError(f"{args.root} is not a directory")
        sizes = [measure(item, root) for item in parse_plan(text)]
    except SliceSizeError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.stdout.write(report(sizes))
    return 0 if all(size.verdict[0] == "fits" for size in sizes) else 1


if __name__ == "__main__":
    sys.exit(main())
