"""The reading of the items of a cycle record that the questions of a process version read: the
item `Discarded attempt` and the item `Review rounds` (`task-cycle/record_template.md`), and the
helpers that cut an item out of the record's lines. `process-audit/audit_count.py` imports it and
gives it the lines of a record it read from git history; the lines are untrusted input and are
read in one pass, with no pattern that tries a line again (WAY-48).

Q1, whether a contradiction with the settlements came out only after the code was written, is read
from two marks and never from the words of the record (WAY-403, WAY-404):

- the item `Discarded attempt` reads `none`, or opens with `reason: ` and one of the markers
  `open design choice`, `reserved choice` and `size` in backticks; a cycle that discarded more than
  one attempt writes nothing beside the colon and only list entries under it, at one indent, one for
  each attempt, each opening so (where the lines are no entries at one indent alone or text stands
  beside the colon, the whole is read as the text of one attempt, which gives no attempt where it
  reads `none` and no answer where it holds a second `reason: ` followed by a backtick, whatever
  word stands there, or opens with no marker, its later lines being details read for that second
  `reason: ` alone); only the first line of an entry is read, and a line
  at the left margin ends the item and is not read; the marker `open design choice` in any of them
  is a yes, `none` and the other two markers no contradiction, and any other text, with no marker at
  its start, gives no answer;
- each entry of the item `Review rounds` opens with ``findings `reports/<file>.md`, contradiction
  yes`` or `no` (a round of fixes, marked by the reviewer's mark of contradiction), or with
  ``review `reports/<file>.md`, PASS`` (a review that passed with no fix, a round with no
  contradiction); an entry that says `yes` is a yes, and an entry of the first form with no such
  mark gives no answer.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-cycle"))
import remarks_check  # noqa: E402  the cutting of a record's lines, shared with its check

# A file of the cycle's `reports/` as `task-cycle/cycle_stages.py` writes it and as the record's
# item `Review rounds` names a findings file: a name that starts with a letter, a digit or `_`,
# holds letters, digits, `_`, `-` and `.`, ends in `.md` and is at most 120 characters long. The
# repetition is bounded and nothing follows it but the end, so no text makes it try again.
REPORT_FILE = re.compile(r"reports/[A-Za-z0-9_][A-Za-z0-9_.-]{0,116}\.md")
ROUNDS_LABEL = "Review rounds"
# The two forms of an entry of the item `Review rounds` (`task-cycle/record_template.md`), each
# read only at the start of the entry's text. The mark of a contradiction is `yes` or `no` and ends
# at the colon or at the end of the text, so that `no longer` is no mark. Every repetition is
# bounded, and nothing is tried again.
ROUND_ENTRY = re.compile(r"findings `([^`\n]{1,200})`(?:, contradiction (yes|no)(?=:|$))?")
REVIEW_ENTRY = re.compile(r"review `([^`\n]{1,200})`, PASS(?=:|$)")
FINDINGS = "findings"
REVIEW = "review"
ITEM_DISCARDED = "Discarded attempt"
# The reason of a discarded attempt, read only at the start of the item's text.
REASON_START = "reason: `"
REASON_MARKER = re.compile(r"reason: `(open design choice|reserved choice|size)`")
OPEN_DESIGN_CHOICE = "open design choice"
NO_ATTEMPT = "none"
SEVERAL = "several"


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


@dataclass(frozen=True)
class Round:
    """An entry of the item `Review rounds`: its form (FINDINGS or REVIEW), the report it names and
    its mark of a contradiction with the settlements, `yes` or `no`, or None where the entry gives
    none."""
    kind: str
    path: str
    contradiction: str | None


def rounds_item(lines: list[str], fenced: list[bool]) -> tuple[list[str] | None, str | None]:
    """The texts of the entries of the record's item `Review rounds`, the ones at its first indent,
    or [] where the item reads `none`; None with the reason where the item is missing, doubled, or
    holds neither `none` nor entries, or text beside its entries. Outside code fences only; one
    pass over the lines."""
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
    return [text for indent, text in markers if indent == base], None


def round_of(text: str) -> Round | None:
    """The entry that `text` is, in one of the two forms, or None. The path stands in the form of a
    file of `reports/`. An entry of the form of a review is a round with no contradiction."""
    entry = ROUND_ENTRY.match(text)
    if entry and is_report_file(entry.group(1)):
        return Round(FINDINGS, entry.group(1), entry.group(2))
    entry = REVIEW_ENTRY.match(text)
    if entry and is_report_file(entry.group(1)):
        return Round(REVIEW, entry.group(1), "no")
    return None


def read_rounds(lines: list[str], fenced: list[bool]) -> tuple[list[Round] | None, str | None]:
    """The entries of the record's item `Review rounds`, in their order, each in one of its two
    forms; [] where the item reads `none`. None with the reason where the item is not in its form,
    an entry is in neither form, or a findings file is named twice."""
    texts, reason = rounds_item(lines, fenced)
    if texts is None:
        return None, reason
    rounds: list[Round] = []
    findings: set[str] = set()
    for text in texts:
        entry = round_of(text)
        if entry is None:
            return None, ("an entry of the item `Review rounds` names no findings file and is no "
                          "review that passed: it opens with neither the word findings and "
                          "reports/<file>.md between backticks nor the word review, "
                          "reports/<file>.md between backticks and PASS")
        if entry.kind == FINDINGS:
            if entry.path in findings:
                return None, "the item `Review rounds` names a findings file twice"
            findings.add(entry.path)
        rounds.append(entry)
    return rounds, None


def review_rounds(lines: list[str], fenced: list[bool]) -> tuple[list[str] | None, str | None]:
    """The findings files of the fix rounds that the record's item `Review rounds` names, in its
    form: the item reading `none`, or nothing after its colon and one entry indented under it for
    each round, opening with the word `findings` and `reports/<file>.md` between backticks. An
    entry of a review that passed with no fix is no fix round and gives no file. None with the
    reason where the item is missing, doubled, or not in that form."""
    rounds, reason = read_rounds(lines, fenced)
    if rounds is None:
        return None, reason
    return [entry.path for entry in rounds if entry.kind == FINDINGS], None


def item_texts(lines: list[str], fenced: list[bool],
               label: str) -> list[tuple[str, list[tuple[str, bool]]]]:
    """The items `- <label>: ...` of a record outside code fences, each as its text on its line and
    the lines indented under it with their fence flags. The whole record is read, since the items
    of the spec and the plan sit below the header. One pass: each item reads down to the next line
    that starts at the margin: a line written there, a continuation of an entry included, is no part
    of the item and is not read."""
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


def discarded_reason(text: str) -> str | None:
    """The reason of a discarded attempt that a text gives: NO_ATTEMPT where it reads `none`, the
    marker where the text opens with `reason: ` and a marker in backticks and holds no other
    `reason: ` followed by a backtick, SEVERAL where it opens with a marker and holds another such
    opening, whatever word stands in its backticks (a text that names two reasons does not say which
    one it is), None otherwise. Only the start of the text is read for
    the marker."""
    if remarks_check.reads_none(text):
        return NO_ATTEMPT
    marker = REASON_MARKER.match(text)
    if marker is None:
        return None
    return marker.group(1) if text.count(REASON_START) == 1 else SEVERAL


def discarded_entries(below: list[tuple[str, bool]]) -> tuple[list[str], bool]:
    """The texts of the list entries at the first indent among the lines under the item
    *Discarded attempt*, outside code fences, and whether they stand alone: the first line is an
    entry at their indent and no plain line stands at their indent or less. A plain line deeper than
    the entries, after the first one, continues one of them; a first line deeper than the entries
    that come after it continues nothing, so the entries are not read as a list."""
    lines = [(remarks_check.indent_of(text), remarks_check.MARKER.fullmatch(text))
             for text, inside in below if not inside]
    markers = [(indent, marker.group("text")) for indent, marker in lines if marker]
    if not markers:
        return [], False
    base = min(indent for indent, _ in markers)
    alone = lines[0][1] is not None and lines[0][0] == base and all(
        marker is not None or indent > base for indent, marker in lines)
    return [text for indent, text in markers if indent == base], alone


def discarded_reasons(rest: str, below: list[tuple[str, bool]]
                      ) -> tuple[list[str | None] | None, str | None]:
    """The reasons of the attempts the item *Discarded attempt* gives, or None with the reason where
    the item is not in a form read. A cycle that discarded one attempt writes it in the text of the
    item, on its line or on the lines under it, the details possibly as a list: one reason, or
    `none`. A cycle that discarded more writes nothing beside the colon and only list entries under
    it, one for each attempt, each opening with its marker; the reason of an entry that reads `none`
    or holds two markers is None; only the first line of an entry is read, so that a marker in a
    deeper line of the entry is a detail and gives nothing. Where a plain line or an entry at
    another indent stands beside the entries, or text stands beside the colon, the whole is read as
    the text of one attempt: it gives that attempt's reason where the text opens with one marker and
    holds no other `reason: ` followed by a backtick (its details may be a list, and a later line
    that names a reason with no backtick after the `reason: `, or in other words, is a detail, not a
    second attempt), and is not read otherwise."""
    entries, alone = discarded_entries(below)
    if entries and alone and not rest.strip():
        return [None if reason in (NO_ATTEMPT, SEVERAL) else reason
                for reason in map(discarded_reason, entries)], None
    reason = discarded_reason(item_words(rest, below))
    if reason == SEVERAL:
        return None, ("the item `Discarded attempt` holds more than one reason in a form that is "
                      "not read: write nothing beside its colon and one entry for each attempt")
    if reason is None and entries and not rest.strip():
        return None, ("a line of the item `Discarded attempt` is no entry or stands at another indent "
                      "than its entries: write each attempt as an entry, all at one indent, and "
                      "nothing else beside them")
    if reason is None:
        return None, ("the item `Discarded attempt` opens with no marker of its reason: it reads "
                      "neither `none` nor `reason: ` and one of open design choice, reserved choice "
                      "and size in backticks")
    return [reason], None


def read_contradiction(lines: list[str], fenced: list[bool]) -> tuple[str | None, str | None]:
    """Q1: whether a contradiction with the settlements came out only after code was written, as
    the marks of the record's item *Review rounds* and of its item *Discarded attempt* give it:
    `yes`, `no`, or None with the reason. It is yes where an entry of a round says
    `contradiction yes` or any reason of the item is `open design choice`; no where every entry
    gives its mark and the item reads `none` or gives only the reasons `reserved choice` and
    `size`."""
    rounds, _ = read_rounds(lines, fenced)
    if rounds and any(entry.contradiction == "yes" for entry in rounds):
        return "yes", None
    items = item_texts(lines, fenced, ITEM_DISCARDED)
    if len(items) != 1:
        return None, item_count_reason(ITEM_DISCARDED, items)
    reasons, why = discarded_reasons(items[0][0], items[0][1])
    if reasons is not None and OPEN_DESIGN_CHOICE in reasons:
        return "yes", None
    if reasons is None:
        return None, why
    if None in reasons:
        return None, "an entry of the item `Discarded attempt` opens with no marker of its reason"
    if rounds is None:
        return None, ("the item `Review rounds` does not give its entries, so whether a review "
                      "round found a contradiction is not known")
    if any(entry.contradiction is None for entry in rounds):
        return None, "the entry of a round does not say whether there was a contradiction"
    return "no", None
