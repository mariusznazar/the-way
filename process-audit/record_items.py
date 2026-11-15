"""The reading of the items of a cycle record that the questions of a process version read: the
item `Discarded attempt` and the item `Review rounds` (`task-cycle/record_template.md`), and the
helpers that cut an item out of the record's lines. `process-audit/audit_count.py` imports it and
gives it the lines of a record it read from git history; the lines are untrusted input and are
read in one pass, with no pattern that tries a line again (WAY-48).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

# A file of the cycle's `reports/` as `task-cycle/cycle_stages.py` writes it and as the record's
# item `Review rounds` names a findings file: a name that starts with a letter, a digit or `_`,
# holds letters, digits, `_`, `-` and `.`, ends in `.md` and is at most 120 characters long. The
# repetition is bounded and nothing follows it but the end, so no text makes it try again.
REPORT_FILE = re.compile(r"reports/[A-Za-z0-9_][A-Za-z0-9_.-]{0,116}\.md")
ROUNDS_LABEL = "Review rounds"
ROUND_ENTRY = re.compile(r"findings `([^`\n]{1,200})`")
ITEM_DISCARDED = "Discarded attempt"
DESIGN_CHOICE = "open design choice"
# Words that deny what follows them, so that `no open design choice` is not read as one.
NEGATIONS = frozenset({"no", "not", "none", "nor", "never", "without", "neither", "nothing"})
WORDS = re.compile(r"[a-z]+")
# A denial is looked for only among the last words just before the phrase, in the same clause: the
# template's own form of a discarded attempt holds `none` and the like in its other parts. At most
# this many characters before the phrase are read, so that the work per phrase is bounded.
DENIAL_WORDS = 4
DENIAL_REACH = 60
CLAUSE_MARKS = frozenset(";:,.—–()[]!?\"")
CONTRACTED_NOT = ("n't", "n’t")


def header_field(line: str) -> tuple[str, str] | None:
    """The label and the value of a header line `- <label>: <value>`, or None. It is cut at the
    first colon in one pass, never by a pattern that could try every way of splitting a run of
    blanks, so that no crafted line costs more than its length."""
    if line[:1] != "-" or line[1:2] not in (" ", "\t"):
        return None
    label, colon, value = line[1:].partition(":")
    label = label.strip(" \t")
    if not colon or not label:
        return None
    return label, value.strip(" \t")


def is_report_file(path: str) -> bool:
    """A file of `reports/` written as `reports/<name>` in the form REPORT_FILE gives, with no
    `..` in it."""
    return REPORT_FILE.fullmatch(path) is not None and ".." not in path


def review_rounds(lines: list[str], fenced: list[bool]) -> tuple[list[str] | None, str | None]:
    """The findings files of the fix rounds that the record's item `Review rounds` names, in its
    form: the item reading `none`, or nothing after its colon and one entry indented under it for
    each round, opening with the word `findings` and `reports/<file>.md` between backticks. None
    with the reason where the item is missing, doubled, or not in that form. Outside code fences
    only; one pass over the lines."""
    openers = [index for index, line in enumerate(lines)
               if not fenced[index] and line.startswith("- ")
               and (header_field(line) or ("", ""))[0] == ROUNDS_LABEL]
    if not openers:
        return None, "the record holds no item `Review rounds`: an earlier form"
    if len(openers) > 1:
        return None, "the record holds the item `Review rounds` more than once"
    start = openers[0]
    rest = header_field(lines[start])[1]
    markers: list[tuple[int, str]] = []
    for line, inside in zip(lines[start + 1:], fenced[start + 1:]):
        if not line.strip():
            continue
        indent = remarks_check.indent_of(line)
        if indent == 0:
            break
        marker = None if inside else remarks_check.MARKER.fullmatch(line)
        if marker:
            markers.append((indent, marker.group("text")))
    if not markers:
        if remarks_check.reads_none(rest):
            return [], None
        return None, ("the item `Review rounds` names no findings file: it reads neither `none` nor "
                      "an entry for each round")
    if rest:
        return None, "the item `Review rounds` holds text beside its entries"
    base = min(indent for indent, _ in markers)
    found: list[str] = []
    for _, text in (marker for marker in markers if marker[0] == base):
        entry = ROUND_ENTRY.match(text)
        if not entry or not is_report_file(entry.group(1)):
            return None, ("an entry of the item `Review rounds` names no findings file: it does not "
                          "open with the word findings and reports/<file>.md between backticks")
        if entry.group(1) in found:
            return None, "the item `Review rounds` names a findings file twice"
        found.append(entry.group(1))
    return found, None


def item_texts(lines: list[str], fenced: list[bool],
               label: str) -> list[tuple[str, list[tuple[str, bool]]]]:
    """The items `- <label>: ...` of a record outside code fences, each as its text on its line and
    the lines indented under it with their fence flags. The whole record is read, since the items
    of the spec and the plan sit below the header. One pass: each item reads down to the next line
    that starts at the margin."""
    found = []
    for index, line in enumerate(lines):
        if fenced[index] or not line.startswith("- "):
            continue
        field_found = header_field(line)
        if field_found is None or field_found[0] != label:
            continue
        below = []
        for next_index in range(index + 1, len(lines)):
            text = lines[next_index]
            if not text.strip():
                continue
            if remarks_check.indent_of(text) == 0:
                break
            below.append((text, fenced[next_index]))
        found.append((field_found[1], below))
    return found


def item_count_reason(label: str, items: list) -> str:
    return (f"the record holds the item `{label}` more than once" if items
            else f"the record holds no item `{label}`")


def item_words(rest: str, below: list[tuple[str, bool]]) -> str:
    """The item's text: its line and the lines under it, joined."""
    return " ".join([rest] + [text.strip() for text, _ in below if text.strip()]).strip()


def reads_none_first(text: str) -> bool:
    """Whether the text opens with the word `none`, as `none on the one-author route` does."""
    word = text.strip(" \t*_`.").casefold()
    return word.startswith("none") and not word[4:5].isalnum()


def read_contradiction(lines: list[str], fenced: list[bool]) -> tuple[str | None, str | None]:
    """Q1: whether a contradiction with the settlements came out only after code was written, as
    the record's item *Discarded attempt* and its *Review rounds* give it: `yes`, `no`, or None with
    the reason."""
    items = item_texts(lines, fenced, ITEM_DISCARDED)
    if len(items) != 1:
        return None, item_count_reason(ITEM_DISCARDED, items)
    text = item_words(items[0][0], items[0][1])
    if remarks_check.reads_none(text):
        findings, why = review_rounds(lines, fenced)
        if findings is None:
            return None, ("the item `Review rounds` does not give its findings files, so whether a "
                          "review round found a contradiction is not known")
        if findings:
            return None, "a review round names findings, and their content is not in the record"
        return "no", None
    if reads_none_first(text):
        # `none` followed by more words, such as `none — no open design choice`, is not read as a
        # discarded open design choice either way.
        return None, "the item `Discarded attempt` opens with none and holds more text"
    folded = text.casefold()
    if DESIGN_CHOICE in folded:
        if any(denied_before(folded, at) for at in phrase_starts(folded)):
            return None, ("the item `Discarded attempt` names an open design choice with a word "
                          "just before it that may deny it")
        return "yes", None
    return None, "the item `Discarded attempt` names neither none nor an open design choice"


def phrase_starts(folded: str) -> list[int]:
    """The place of each occurrence of the phrase in the case-folded text, one pass."""
    found = []
    at = folded.find(DESIGN_CHOICE)
    while at != -1:
        found.append(at)
        at = folded.find(DESIGN_CHOICE, at + len(DESIGN_CHOICE))
    return found


def denied_before(folded: str, at: int) -> bool:
    """Whether a denying word stands among the last words just before the phrase at `at`, in the
    same clause: at most DENIAL_REACH characters are read, cut after the last clause mark, and the
    last DENIAL_WORDS words of what remains are searched. Linear: no pattern is tried again."""
    before = folded[max(0, at - DENIAL_REACH):at]
    for index in range(len(before) - 1, -1, -1):
        if before[index] in CLAUSE_MARKS:
            before = before[index + 1:]
            break
    if any(mark in before for mark in CONTRACTED_NOT):
        return True
    return bool(NEGATIONS.intersection(WORDS.findall(before)[-DENIAL_WORDS:]))
