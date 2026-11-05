"""The form of the description of a request a task cycle opens: the headings of
`task-cycle/skill/request_template.md` in their order and level, content or `none` in each section,
and the collapsed block that repeats the top part in the task document's language.

Usage:

    python -B task-cycle/request_check.py DESCRIPTION --task TASK

In a product, the path starts with `.the-way/`. DESCRIPTION is the description file,
`.runs/task-cycles/<task-slug>/request.md`. TASK is the frozen task document of the cycle's record,
or, for a change to the-way made without a cycle, the task document or the project plan the change
carries out.

The description is read as the template gives it:

- its first line that is not blank reads `**State: ready|draft|blocked** — <why>`;
- the sections are the `##` headings of TOP_HEADINGS and LOWER_HEADINGS, once each and in that
  order, the task's own sections, any number of `##` headings of their own, standing only between
  the last two headings of LOWER_HEADINGS; `### Underneath` stands in `## What you will see`;
- the block is the one `<details>` element whose opening line comes after `## How to merge` and
  before `## Technical changes`; its content is the text after its `</summary>` up to the
  `</details>` that closes it, nested elements counted;
- a line in fenced code or inside any `<details>` element is never a heading, and only ATX
  headings count;
- a section, `### Underneath` and the block each hold content: a line that is not blank and not
  only an HTML comment, `none` included.

The language of a text is measured by the share of its words that are English function words, from
a list that leaves out every word that is also a common Polish word; code, URLs, link targets and
HTML tags are not counted. A text of fewer than MINIMUM_WORDS words is not judged; one whose share
reaches ENGLISH_THRESHOLD is English. TASK is measured on its title line and the content of its
`### Need` and `### To do`, or, where it holds neither heading, as a project plan: on the *Goal*
cells of its `## Tasks` table and the question text of each item of its `## Open questions`, the
text before its first ` — `, since a plan keeps every other marker and state in English. Where TASK
is English, the block reads `none`; where it is not, the block does not read `none` and its text is
not English. Where TASK or the block is not judged, no error follows from its language.

The script judges no content: not whether the decision section is complete or true, not the plain
words of the top part, not whether the block says what the top part says or which language other
than English it is in, not the items of the lower part and not the task's own sections.

Each problem is printed on stdout as `line <n>: <what is wrong and what to write>`, in the order of
the file, then one summary line naming the sections found and the reading of the languages. Exit
code: 0 when the form holds; 1 with the problems listed; 2 with `Error: <message>` on stderr when
an argument is wrong or a file cannot be read as UTF-8. The script reads the two files and nothing
else, runs nothing and writes no file.

Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

TOP_HEADINGS = ("What you will see", "For you to decide", "Cost", "How to merge")
LOWER_HEADINGS = ("Technical changes", "Checks", "Foundation entries", "Minor findings",
                  "Findings outside the task's scope", "Course of the cycle")
UNDERNEATH = "Underneath"
# The heading the template's skeleton gives in the place of the task's own sections.
OWN_SECTIONS_PLACEHOLDER = "<…>"
HEADINGS = TOP_HEADINGS + LOWER_HEADINGS
# The task's own sections stand after this heading and before the last one.
OWN_SECTIONS_AFTER = LOWER_HEADINGS[-2]
BLOCK_AFTER = TOP_HEADINGS[-1]
BLOCK_BEFORE = LOWER_HEADINGS[0]
STATES = ("ready", "draft", "blocked")

# English function words, none of them also a common Polish word: `a`, `i`, `to`, `on`, `no`,
# `do`, `by`, `we`, `my`, `me`, `was`, `same`, `most` and `mine` are left out.
FUNCTION_WORDS = frozenset("""
    the an of and or but nor if then than that this these those there here which what who whom
    whose when where why how is are were be been being am has have had having does did will would
    shall should can could may might must it its they them their theirs he him his she her hers
    you your yours our ours us in into onto at as for from with within without about after before
    under over between through during until since because while each every any some all both
    either neither such other another only also not so too very just more own again once
""".split())
ENGLISH_THRESHOLD = 0.2
MINIMUM_WORDS = 20

STATE_LINE = re.compile(r"\*\*State: (\w+)\*\* — (.*)")
HEADING = re.compile(r" {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*")
FENCE = re.compile(r" {0,3}(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"(`+).+?\1")
DETAILS_OPEN = re.compile(r"<details(?=[\s>])", re.I)
DETAILS_CLOSE = re.compile(r"</details\s*>", re.I)
SUMMARY_CLOSE = re.compile(r"</summary\s*>", re.I)
COMMENT = re.compile(r"<!--.*?(?:-->|\Z)", re.S)
FENCED_TEXT = re.compile(r"^ {0,3}(`{3,}|~{3,}).*?(?:^ {0,3}\1[`~]*[ \t]*$|\Z)", re.S | re.M)
URL = re.compile(r"<?https?://\S+")
LINK_TARGET = re.compile(r"\]\([^)]*\)")
TAG = re.compile(r"<[^>]*>")
WORD = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)?")


class RequestCheckError(Exception):
    """An argument that is wrong or a file that cannot be read."""


class Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # type: ignore[override]
        raise RequestCheckError(message)


def display(value: object) -> str:
    """Keep text taken from the files inside one report line."""
    return "".join(char if char.isprintable() else ascii(char)[1:-1] for char in str(value))


@dataclass
class Line:
    number: int
    text: str
    in_fence: bool
    depth: int  # `<details>` elements open before this line
    opens: int
    closes: int
    forced: bool  # an element left open ends before this line


@dataclass
class Heading:
    number: int
    level: int
    text: str


@dataclass
class Element:
    start: int  # index in the list of lines
    end: int  # index of its last line
    closed: bool


@dataclass
class Result:
    problems: list[tuple[int, str]] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)
    task_language: str = "not judged"
    task_words: int = 0
    block_language: str = "not judged"
    block_words: int = 0


def split_lines(text: str) -> list[str]:
    lines = re.split(r"\r\n|\r|\n", text)
    return lines[:-1] if lines and lines[-1] == "" else lines


def scan(text: str, forced: frozenset[int] = frozenset()) -> list[Line]:
    """Each line, with whether it stands in fenced code and how deep in `<details>` it stands.

    A line of `forced` closes every element still open before it.
    """
    lines = []
    fence = ""
    depth = 0
    for number, raw in enumerate(split_lines(text), 1):
        if number in forced:
            depth = 0
        match = FENCE.match(raw)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence) \
                    and not raw.strip().strip(fence[0]):
                fence = ""
            lines.append(Line(number, raw, True, depth, 0, 0, number in forced))
            continue
        if match:
            fence = match.group(1)
            lines.append(Line(number, raw, True, depth, 0, 0, number in forced))
            continue
        bare = CODE_SPAN.sub("", raw)
        opens, closes = len(DETAILS_OPEN.findall(bare)), len(DETAILS_CLOSE.findall(bare))
        lines.append(Line(number, raw, False, depth, opens, closes, number in forced))
        depth = max(0, depth + opens - closes)
    return lines


def heading_of(line: Line) -> Heading | None:
    if line.in_fence or line.depth or line.opens:
        return None
    match = HEADING.fullmatch(line.text)
    if not match:
        return None
    return Heading(line.number, len(match.group(1)), (match.group(2) or "").strip())


def headings(lines: list[Line]) -> list[Heading]:
    return [heading for heading in map(heading_of, lines) if heading]


def elements(lines: list[Line]) -> list[Element]:
    """The `<details>` elements that stand inside no other."""
    found = []
    open_element = None
    depth = 0
    for index, line in enumerate(lines):
        if line.forced and open_element:
            open_element.end = index - 1
            open_element = None
            depth = 0
        if line.in_fence:
            continue
        if not depth and line.opens:
            open_element = Element(index, len(lines) - 1, False)
            found.append(open_element)
        depth = max(0, depth + line.opens - line.closes)
        if open_element and not depth:
            open_element.end = index
            open_element.closed = True
            open_element = None
    return found


def scan_description(text: str) -> list[Line]:
    """The lines of a description, an element left open ending before the next `##` heading of
    the template, so that one missing `</details>` does not hide the rest of the description."""
    forced: frozenset[int] = frozenset()
    while True:
        lines = scan(text, forced)
        added = set()
        for element in elements(lines):
            if element.closed:
                continue
            for line in lines[element.start + 1:]:
                match = None if line.in_fence else HEADING.fullmatch(line.text)
                if match and len(match.group(1)) == 2 and (match.group(2) or "").strip() in HEADINGS \
                        and line.number not in forced:
                    added.add(line.number)
                    break
        if not added:
            return lines
        forced = forced | added


def has_content(text: str) -> bool:
    return any(line.strip() for line in COMMENT.sub("", text).splitlines())


def block_content(lines: list[Line], element: Element) -> str:
    text = "\n".join(line.text for line in lines[element.start:element.end + 1])
    summary = SUMMARY_CLOSE.search(text)
    if summary:
        text = text[summary.end():]
    else:
        text = text[text.index(">", DETAILS_OPEN.search(text).start()) + 1:]
    closes = list(DETAILS_CLOSE.finditer(text))
    return text[:closes[-1].start()] if closes else text


def reads_none(text: str) -> bool:
    return COMMENT.sub("", text).strip().strip("`").strip() == "none"


def english_share(text: str) -> tuple[float, int]:
    """The share of the words of `text` that are English function words, and its count of words."""
    for pattern in (COMMENT, FENCED_TEXT, CODE_SPAN, URL, LINK_TARGET, TAG):
        text = pattern.sub(" ", text)
    words = [word.lower() for word in WORD.findall(text)]
    if not words:
        return 0.0, 0
    return sum(word in FUNCTION_WORDS for word in words) / len(words), len(words)


def language(text: str) -> tuple[str, int]:
    share, words = english_share(text)
    if words < MINIMUM_WORDS:
        return "not judged", words
    return ("English" if share >= ENGLISH_THRESHOLD else "not English"), words


def section_text(task: str, title: str) -> str | None:
    """The content of the section of `task` under the heading `title`, up to the next heading."""
    lines = scan(task)
    found = None
    for heading in headings(lines):
        if found is not None:
            return "\n".join(line.text for line in lines[found:heading.number - 1])
        if heading.text == title:
            found = heading.number
    return None if found is None else "\n".join(line.text for line in lines[found:])


def plan_text(task: str) -> str:
    """The *Goal* cells of a plan's `## Tasks` and the questions of its `## Open questions`."""
    parts = []
    rows = [line.strip() for line in (section_text(task, "Tasks") or "").splitlines()
            if line.strip().startswith("|")]
    if rows:
        columns = [cell.strip() for cell in rows[0].strip("|").split("|")]
        if "Goal" in columns:
            goal = columns.index("Goal")
            for row in rows[2:]:
                cells = [cell.strip() for cell in row.strip("|").split("|")]
                if goal < len(cells):
                    parts.append(cells[goal])
    for line in (section_text(task, "Open questions") or "").splitlines():
        item = re.match(r"\s*[-*]\s+(.*)", line)
        if item:
            parts.append(item.group(1).split(" — ")[0])
    return "\n".join(parts)


def task_text(task: str) -> str:
    """The text of TASK whose language is measured."""
    need, to_do = section_text(task, "Need"), section_text(task, "To do")
    if need is None and to_do is None:
        return plan_text(task)
    title = next((heading.text for heading in headings(scan(task)) if heading.level == 1), "")
    return "\n".join([title, need or "", to_do or ""])


def check_state(lines: list[Line], problems: list[tuple[int, str]]) -> None:
    first = next((line for line in lines if line.text.strip()), None)
    expected = ("write `**State: ready|draft|blocked** — <why, in one sentence>` as the first "
                "line")
    if first is None:
        problems.append((1, f"the description is empty; {expected}"))
        return
    match = STATE_LINE.fullmatch(first.text.strip())
    if not match:
        problems.append((first.number, f"the first line gives no state; {expected}"))
    elif match.group(1) not in STATES:
        problems.append((first.number, f"`{display(match.group(1))}` is no state; the state is "
                                       f"one of {', '.join(STATES)}"))
    elif not match.group(2).strip():
        problems.append((first.number, "the state gives no reason; write why after the dash, in "
                                       "one sentence"))


def check(description: str, task: str) -> Result:
    """The problems of the form of `description`, a request's description for the task `task`."""
    result = Result()
    problems = result.problems
    lines = scan_description(description)
    end_line = len(lines) + 1
    check_state(lines, problems)

    # The `##` headings: those of the template once each and in order, the task's own in their slot.
    sections = [heading for heading in headings(lines) if heading.level == 2]
    seen: dict[str, Heading] = {}
    kept: list[Heading] = []
    last = -1
    for heading in sections:
        name = display(heading.text)
        if heading.text in HEADINGS:
            index = HEADINGS.index(heading.text)
            if heading.text in seen:
                problems.append((heading.number, f"`## {name}` is repeated; it stands once, at "
                                                 f"line {seen[heading.text].number}"))
                continue
            if index < last:
                problems.append((heading.number, f"`## {name}` is out of order; move it before "
                                                 f"`## {HEADINGS[last]}`"))
            else:
                last = index
            seen[heading.text] = heading
            kept.append(heading)
        elif last == HEADINGS.index(OWN_SECTIONS_AFTER):
            kept.append(heading)
        else:
            problems.append((heading.number, f"`## {name}` is not a heading of the template; a "
                                             f"task's own section stands between `## "
                                             f"{OWN_SECTIONS_AFTER}` and `## {HEADINGS[-1]}`"))
    for index, name in enumerate(HEADINGS):
        if name not in seen:
            following = [seen[later].number for later in HEADINGS[index + 1:] if later in seen]
            problems.append((min(following, default=end_line),
                             f"`## {name}` is missing; write it here, with its content or `none`"))
    result.sections = [heading.text for heading in kept]

    # The block: the one top-level `<details>` between `## How to merge` and `## Technical changes`.
    after = seen[BLOCK_AFTER].number if BLOCK_AFTER in seen else 0
    before = seen[BLOCK_BEFORE].number if BLOCK_BEFORE in seen else end_line
    found = elements(lines)
    for element in found:
        if not element.closed:
            problems.append((lines[element.start].number, "this `<details>` is not closed; write "
                                                          "`</details>` after its content"))
    candidates = [element for element in found if after < lines[element.start].number < before]
    if not candidates:
        problems.append((before, "no block; write `<details>`, a `<summary>` and the top part in "
                                 "the task document's language, or `none` where the task is in "
                                 "English, directly after the content of `## How to merge`"))
    for extra in candidates[1:]:
        problems.append((lines[extra.start].number, "a second block; the top part stands once in "
                                                    "the task's language, in one `<details>`"))
    block = candidates[0] if candidates else None
    block_lines = (set() if block is None else
                   set(range(lines[block.start].number, lines[block.end].number + 1)))

    # The content of each section, and of `### Underneath` in `## What you will see`.
    bounds = [heading.number for heading in sections] + [end_line]
    for heading in kept:
        stop = min(number for number in bounds if number > heading.number)
        body = [line for line in lines[heading.number:stop - 1] if line.number not in block_lines]
        name = display(heading.text)
        if heading.text == TOP_HEADINGS[0]:
            under = next((sub for sub in headings(lines) if sub.level == 3
                          and sub.text == UNDERNEATH and heading.number < sub.number < stop), None)
            if under is None:
                problems.append((heading.number, f"`### {UNDERNEATH}` is missing from `## "
                                                 f"{name}`; write it there, with one or two "
                                                 f"sentences on what is under the change"))
            else:
                if not has_content("\n".join(line.text for line in body
                                             if line.number < under.number)):
                    problems.append((heading.number, f"`## {name}` has no content before `### "
                                                     f"{UNDERNEATH}`; write what changes, or "
                                                     f"`none`"))
                if not has_content("\n".join(line.text for line in body
                                             if line.number > under.number)):
                    problems.append((under.number, f"`### {UNDERNEATH}` has no content; write "
                                                   f"what is under the change, or `none`"))
                continue
        if not has_content("\n".join(line.text for line in body)):
            problems.append((heading.number, f"`## {name}` has no content; write it, or `none`"))

    # The languages of the task and of the block.
    result.task_language, result.task_words = language(task_text(task))
    if block is not None and block.closed:
        content = block_content(lines, block)
        number = lines[block.start].number
        result.block_language, result.block_words = language(content)
        if not has_content(content):
            problems.append((number, "the block has no content; write the top part in the task "
                                     "document's language, or `none` where the task is in "
                                     "English"))
        elif result.task_language == "English" and not reads_none(content):
            problems.append((number, "the task document is in English; the block reads `none`"))
        elif result.task_language == "not English" and reads_none(content):
            problems.append((number, "the task document is not in English; write the top part "
                                     "in its language in the block, instead of `none`"))
        elif result.task_language == "not English" and result.block_language == "English":
            problems.append((number, "the block is in English; write the top part in the task "
                                     "document's language"))
    problems.sort(key=lambda problem: problem[0])
    return result


def summary(result: Result) -> str:
    found = ", ".join(display(name) for name in result.sections) or "none"
    head = ("form holds" if not result.problems else
            f"{len(result.problems)} problem{'s' if len(result.problems) != 1 else ''}")

    def reading(name: str, value: str, words: int) -> str:
        if value == "not judged":
            return f"{name}: not judged, {words} words, fewer than {MINIMUM_WORDS}"
        return f"{name}: {value}, {words} words"

    return (f"{head}; sections: {found}; "
            f"{reading('task', result.task_language, result.task_words)}; "
            f"{reading('block', result.block_language, result.block_words)}")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise RequestCheckError(f"cannot read {display(path)} as UTF-8: {display(error)}") from error


def main(argv: list[str] | None = None) -> int:
    parser = Parser(description=__doc__.split("\n\n")[0])
    parser.add_argument("description", type=Path, metavar="DESCRIPTION")
    parser.add_argument("--task", type=Path, required=True, metavar="TASK")
    try:
        args = parser.parse_args(argv)
        result = check(read(args.description), read(args.task))
    except RequestCheckError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    for number, message in result.problems:
        sys.stdout.write(f"line {number}: {message}\n")
    sys.stdout.write(summary(result) + "\n")
    return 1 if result.problems else 0


if __name__ == "__main__":
    sys.exit(main())
