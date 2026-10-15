"""The check of a project plan: what a script can decide of a plan that breaks an approved project
definition into tasks (WAY-142, WAY-146; invariants `project-plan-form/1`, `project-plan-check/1`).

Usage, from any directory:

    python -B <the-way>/project-level/plan_check.py PLAN

The plan follows `project-level/plan/template.md`; the definition it names on its `Definition:`
line, by a path relative to the plan, follows `project-level/definition_template.md`. The check
reports:

- form — a `Status:` line reading `draft` or `handed over YYYY-MM-DD`, a calendar date; a line
  `Definition: <path> — fingerprint <8 lower-case hex digits>` naming a definition that can be
  read, whose In scope reads `none` or holds a top-level list item, and whose gate record and text
  both give that fingerprint; the sections `## Tasks`, `## Projected entries`, `## Open questions`,
  `## Phases`, `## Change log` once each, in this order, with no other second-level heading and
  none of them empty; the tasks table and the projected entries table with the template's header
  rows, a separator row of as many cells, and every cell in its form, numbers in ASCII digits and
  `\\|` standing for a literal `|`; no task number or name held twice; a state
  `done — goal delivered in task <n>` naming another task the plan holds. "Projected entries"
  reads `none` only where the definition projects no entry;
- entries — every projected heading of the definition stands in exactly one row, word for word,
  every row names a projected heading, every task a row names is held by the plan, and the task
  that writes an entry is among those that realize it;
- scope — every item of the definition's In scope (its top-level list items, whatever their
  marker, numbered from 1) is named by a task, and no task names an item above their count;
- dependencies — no task depends on a task the plan does not hold, or on itself, directly or
  through other tasks;
- preparatory — every preparatory task has a task depending on it;
- questions — every open question of the definition stands once, word for word, with the place
  the definition gives it, followed by a task of the plan or a non-empty answer; every item is in
  one of these forms, and an item naming a place of the definition belongs to a question it holds.

A finding of form that makes a part of the plan unreadable stops the checks of that part; what can
still be read is checked. Each finding prints as `fail: <condition> — line <n>: <message>`, n
being the line of the plan (0 where no line applies), sorted by line, and a last line
`plan: nothing found` or `plan: <k> finding(s)`. Exit codes: 0 nothing found, 1 findings, 2 the
call is wrong or the plan cannot be read. A definition that cannot be read is a finding of form.
The check judges nothing the plan's critique judges: whether a goal is checkable in the running
product, where a technical element enters, whether a moved question has its reason in the change
log, or whether an answer settles its question.
"""

import argparse
import datetime
import os
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, HERE)
import readiness_check  # noqa: E402
from readiness_check import FENCE, content, items, split  # noqa: E402

TASKS = "Tasks"
ENTRIES = "Projected entries"
QUESTIONS = "Open questions"
PHASES = "Phases"
CHANGE_LOG = "Change log"
SECTIONS = (TASKS, ENTRIES, QUESTIONS, PHASES, CHANGE_LOG)

TASK_COLUMNS = ("#", "Task", "Goal", "Depends on", "In scope", "Preparatory", "State", "Document")
ENTRY_COLUMNS = ("Entry", "Realized by", "Written by")

STATUS = re.compile(r"^Status: (draft|handed over (?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}))$")
DEFINITION_LINE = re.compile(r"^Definition: (?P<path>\S.*?) — fingerprint "
                             r"(?P<fingerprint>[0-9a-f]{8})$")
DATED_ITEM = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2} — \S")
SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+$")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
NUMBER = re.compile(r"^[1-9][0-9]*$")  # ASCII digits only: `\d` takes every Unicode digit
NUMBERS = re.compile(r"^[1-9][0-9]*(, [1-9][0-9]*)*$")
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DELIVERED_IN = re.compile(r"^done — goal delivered in task (?P<task>[1-9][0-9]*)$")
STATES = ("to refine", "waiting for human", "ready for cycle", "in cycle", "done",
          "dropped — approved by human")
NO_NUMBER = "—"
PROJECTED_ENTRY = re.compile(r"^#### (.+?)\s*$")
TOP_LEVEL_ITEM = re.compile(r"^([-*+]|[0-9]+[.)])[ \t]+\S")
RULE = re.compile(r"^ {0,3}([-*_])([ \t]*\1){2,}[ \t]*$")  # a horizontal rule is no item
RESOLVED_IN = " — resolved in: "
PLAN_QUESTION = re.compile(r"^(?P<question>.+?) — definition: (?P<place>.+?) — "
                           r"(?:plan: task (?P<task>.*)|answer:(?: (?P<answer>.*))?)$")
RAISED = "none"
GATE_FINGERPRINT = readiness_check.GATE_LINES[2][1]
DEFINITION_NEEDS = ("Goal", "In scope", readiness_check.OPEN_QUESTIONS, readiness_check.PROJECTED,
                    readiness_check.GATE_RECORD)


@dataclass
class Finding:
    condition: str
    line: int
    message: str

    def __str__(self):
        return "fail: %s — line %d: %s" % (self.condition, self.line, self.message)


@dataclass
class Task:
    line: int
    number: int | None = None
    name: str | None = None
    depends: list | None = None
    scope: list | None = None
    preparatory: bool | None = None
    delivered_in: int | None = None
    state: str | None = None
    document: str | None = None


@dataclass
class Entry:
    line: int
    entry: str
    realized: list | None = None
    written: int | None = None


@dataclass
class Plan:
    """What the check could read of a plan; None where a finding of form made it unreadable."""
    sections: dict = field(default_factory=dict)  # name -> Section, for a section standing once
    tasks: list | None = None
    numbers_known: bool = False  # every task row gives a readable number
    entries: list | None = None


@dataclass
class Definition:
    """What the plan check reads of a definition."""
    in_scope: int | None  # the number of In scope items, None where they cannot be numbered
    questions: list  # (question, place)
    projected: list  # projected headings, in order


def calendar_date(text):
    try:
        datetime.date.fromisoformat(text)
    except ValueError:
        return False
    return True


def definition_path(plan_text):
    """The path the plan's `Definition:` line names, or None where no line in its form stands."""
    preamble, _ = split(plan_text)
    for _, line in preamble:
        if line.startswith("Definition:"):
            match = DEFINITION_LINE.match(line.rstrip())
            return match.group("path") if match else None
    return None


# --- The header -------------------------------------------------------------------------------


def check_header(preamble, definition_text, definition_error):
    """Return the findings of the header, and the definition read, or None where it cannot be."""
    findings = []
    status = [(n, line) for n, line in preamble if line.startswith("Status:")]
    if not status:
        findings.append(Finding("form", 0, "no `Status:` line above the first section"))
    elif not (match := STATUS.match(status[0][1].rstrip())):
        findings.append(Finding("form", status[0][0], "the status reads neither `draft` nor "
                                "`handed over YYYY-MM-DD`"))
    elif match.group("date") and not calendar_date(match.group("date")):
        findings.append(Finding("form", status[0][0], "the plan was handed over on %s, which is "
                                "no calendar date" % match.group("date")))
    lines = [(n, line) for n, line in preamble if line.startswith("Definition:")]
    if not lines:
        findings.append(Finding("form", 0, "no `Definition: <path> — fingerprint <hex>` line "
                                "above the first section"))
        return findings, None
    number, line = lines[0]
    match = DEFINITION_LINE.match(line.rstrip())
    if not match:
        findings.append(Finding("form", number, "the line is not `Definition: <path> — "
                                "fingerprint <8 lower-case hexadecimal digits>`"))
        return findings, None
    if definition_text is None:
        reason = ": %s" % definition_error if definition_error else ""
        path = match.group("path")
        findings.append(Finding("form", number, "the definition %s cannot be read%s"
                                % (path if path.isprintable() else repr(path), reason)))
        return findings, None
    _, sections = split(definition_text)
    names = [s.name for s in sections]
    unread = [name for name in DEFINITION_NEEDS if names.count(name) != 1]
    if unread or names.index("Goal") > names.index(readiness_check.GATE_RECORD):
        findings.append(Finding("form", number, "the definition %s is not in its form: %s"
                                % (match.group("path"), ", ".join("`## %s` does not stand once"
                                                                  % name for name in unread)
                                   or "`## Goal` stands after `## Gate record`")))
        return findings, None
    by_name = {s.name: s for s in sections}
    held = match.group("fingerprint")
    gate = [m.group(1) for _, l in by_name[readiness_check.GATE_RECORD].lines
            if (m := GATE_FINGERPRINT.match(l.rstrip()))]
    if not gate:
        findings.append(Finding("form", number, "the definition's gate record holds no line "
                                "`- Definition fingerprint: <hex>` — the definition has not "
                                "passed its readiness gate"))
    elif gate[0] != held:
        findings.append(Finding("form", number, "the fingerprint %s is not the one the "
                                "definition's gate record holds, %s" % (held, gate[0])))
    text_fingerprint = readiness_check.definition_fingerprint(definition_text)
    if text_fingerprint != held:
        findings.append(Finding("form", number, "the fingerprint %s is not the one the "
                                "definition's text gives, %s — the plan stands on nothing until "
                                "the definition passes its gate again and the plan is checked "
                                "against it" % (held, text_fingerprint)))
    definition = read_definition(by_name)
    if definition.in_scope is None:
        findings.append(Finding("form", number, "the definition's In scope reads neither `none` "
                                "nor holds a top-level list item — its items cannot be "
                                "numbered"))
    return findings, definition


def top_level_items(section):
    """The number of top-level list items of a section, whatever their marker. A nested list, a
    heading, a sentence and a fenced block are no item."""
    count, fenced = 0, False
    for _, line in section.lines:
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and TOP_LEVEL_ITEM.match(line) and not RULE.match(line):
            count += 1
    return count


def read_definition(by_name):
    """Read what the plan answers to; `in_scope` is None where In scope is not `none` and holds
    no top-level list item, so that the plan's numbers name nothing."""
    scope = by_name["In scope"]
    if [line.strip() for _, line in content(scope)] == ["none"]:
        in_scope = 0
    else:
        in_scope = top_level_items(scope) or None
    questions = []
    open_questions = by_name[readiness_check.OPEN_QUESTIONS]
    if [line.strip() for _, line in content(open_questions)] != ["none"]:
        for _, text in items(open_questions):
            if text is not None and RESOLVED_IN in text:
                question, place = text.split(RESOLVED_IN, 1)
                questions.append((question, place))
    projected, fenced = [], False
    for _, line in by_name[readiness_check.PROJECTED].lines:
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and (match := PROJECTED_ENTRY.match(line)):
            projected.append(match.group(1))
    return Definition(in_scope, questions, projected)


# --- The sections -----------------------------------------------------------------------------


def check_sections(sections):
    """Return the findings of the sections, and the sections standing once by their names."""
    findings = []
    names = [s.name for s in sections]
    for index, section in enumerate(sections):
        if section.name not in SECTIONS:
            findings.append(Finding("form", section.heading_line,
                                    "`## %s` is no section of the plan" % section.name))
        elif names.index(section.name) != index:
            findings.append(Finding("form", section.heading_line,
                                    "`## %s` stands a second time" % section.name))
    for name in SECTIONS:
        if name not in names:
            findings.append(Finding("form", 0, "the section `## %s` is missing" % name))
    known = [name for name in dict.fromkeys(names) if name in SECTIONS]
    if known != [name for name in SECTIONS if name in known]:
        line = next(s.heading_line for s in sections if s.name in SECTIONS)
        findings.append(Finding("form", line, "the sections stand out of the template's order: "
                                "%s" % ", ".join(known)))
    once = {s.name: s for s in sections if s.name in SECTIONS and names.count(s.name) == 1}
    for section in once.values():
        if not content(section):
            findings.append(Finding("form", section.heading_line, "`## %s` is empty — write "
                                    "`none` where nothing is there" % section.name))
    if CHANGE_LOG in once and content(once[CHANGE_LOG]):
        if not any(text is not None and DATED_ITEM.match(text)
                   for _, text in items(once[CHANGE_LOG])):
            findings.append(Finding("form", once[CHANGE_LOG].heading_line, "`## %s` holds no item "
                                    "`- YYYY-MM-DD — <what changed>`" % CHANGE_LOG))
    return findings, once


# --- The tables -------------------------------------------------------------------------------


def cells(line):
    """The cells of a table row, or None where the line is not one."""
    line = line.strip()
    if len(line) < 2 or not (line.startswith("|") and line.endswith("|")):
        return None
    return [cell.strip().replace("\\|", "|") for cell in CELL_SPLIT.split(line[1:-1])]


def read_table(section, columns):
    """Return the findings of a section's table, and its rows as (line, cells), or None where the
    table cannot be read."""
    lines = content(section)
    header = "| " + " | ".join(columns) + " |"
    if not lines or not lines[0][1].lstrip().startswith("|"):
        return [Finding("form", section.heading_line,
                        "`## %s` holds no table" % section.name)], None
    number, first = lines[0]
    if first.strip() != header:
        return [Finding("form", number, "the header row of `## %s` is not `%s`"
                        % (section.name, header))], None
    findings, rows = [], []
    rest = lines[1:]
    if rest and SEPARATOR.match(rest[0][1].strip()):
        separator_number, separator = rest[0]
        rest = rest[1:]
        if len(cells(separator)) != len(columns):
            findings.append(Finding("form", separator_number, "the separator row holds %d cells, "
                                    "not the %d columns of `## %s`"
                                    % (len(cells(separator)), len(columns), section.name)))
    else:
        findings.append(Finding("form", number, "no separator row `|---|` under the header row "
                                "of `## %s`" % section.name))
    for number, line in rest:
        row = cells(line)
        if row is None:
            findings.append(Finding("form", number, "a line under `## %s` that is no row of its "
                                    "table" % section.name))
        elif len(row) != len(columns):
            findings.append(Finding("form", number, "the row holds %d cells, not the %d columns "
                                    "of `## %s`" % (len(row), len(columns), section.name)))
        else:
            rows.append((number, row))
    return findings, rows


def number_list(value):
    return [int(n) for n in value.split(", ")]


def read_tasks(section):
    findings, rows = read_table(section, TASK_COLUMNS)
    if rows is None:
        return findings, None, False
    if not rows:
        findings.append(Finding("form", section.heading_line, "the tasks table holds no task"))
    tasks = []
    for line, row in rows:
        values = dict(zip(TASK_COLUMNS, row))
        task = Task(line)
        task.state = values["State"]
        task.document = values["Document"]

        def off(column, form):
            findings.append(Finding("form", line, "`%s` reads `%s`, not %s"
                                    % (column, values[column], form)))

        if NUMBER.match(values["#"]):
            task.number = int(values["#"])
        else:
            off("#", "a positive integer")
        if NAME.match(values["Task"]):
            task.name = values["Task"]
        else:
            off("Task", "lower-case letters and digits in words joined by single hyphens")
        if not values["Goal"]:
            findings.append(Finding("form", line, "`Goal` is empty"))
        for column, attribute in (("Depends on", "depends"), ("In scope", "scope")):
            value = values[column]
            if value == NO_NUMBER:
                setattr(task, attribute, [])
            elif NUMBERS.match(value):
                setattr(task, attribute, number_list(value))
            else:
                off(column, "`—` or positive integers separated by `, `")
        if values["Preparatory"] in ("yes", "no"):
            task.preparatory = values["Preparatory"] == "yes"
        else:
            off("Preparatory", "`yes` or `no`")
        delivered = DELIVERED_IN.match(values["State"])
        if delivered:
            task.delivered_in = int(delivered.group("task"))
        elif values["State"] not in STATES:
            off("State", "a state of the template's list")
        if not values["Document"]:
            findings.append(Finding("form", line, "`Document` is empty — write `—` until the "
                                    "task has a document"))
        tasks.append(task)
    seen_numbers, seen_names = set(), set()
    for task in tasks:
        if task.number is not None:
            if task.number in seen_numbers:
                findings.append(Finding("form", task.line, "the number %d is held by another "
                                        "task" % task.number))
            seen_numbers.add(task.number)
        if task.name is not None:
            if task.name in seen_names:
                findings.append(Finding("form", task.line, "the name `%s` is held by another "
                                        "task" % task.name))
            seen_names.add(task.name)
    for task in tasks:
        if task.delivered_in is not None and task.delivered_in == task.number:
            findings.append(Finding("form", task.line, "the state names the task itself as the "
                                    "one that delivered its goal"))
    numbers_known = all(task.number is not None for task in tasks)
    if numbers_known:
        for task in tasks:
            if task.delivered_in is not None and task.delivered_in not in seen_numbers:
                findings.append(Finding("form", task.line, "the state names task %d, which the "
                                        "plan does not hold" % task.delivered_in))
    return findings, tasks, numbers_known


def read_entries(section, definition):
    """Return the findings of the projected entries table, and its rows, or None where the section
    reads `none` or its table cannot be read."""
    lines = [line.strip() for _, line in content(section)]
    if lines == ["none"]:
        if definition is not None and definition.projected:
            return [Finding("form", section.heading_line, "`## %s` reads `none`, while the "
                            "definition projects %d entries"
                            % (ENTRIES, len(definition.projected)))], None
        return [], None
    findings, rows = read_table(section, ENTRY_COLUMNS)
    if rows is None:
        return findings, None
    entries = []
    for line, (name, realized, written) in rows:
        entry = Entry(line, name)
        if NUMBERS.match(realized):
            entry.realized = number_list(realized)
        else:
            findings.append(Finding("form", line, "`Realized by` reads `%s`, not positive "
                                    "integers separated by `, `" % realized))
        if NUMBER.match(written):
            entry.written = int(written)
        else:
            findings.append(Finding("form", line, "`Written by` reads `%s`, not the number of "
                                    "one task" % written))
        entries.append(entry)
    return findings, entries


# --- The checks against the definition and within the plan ------------------------------------


def check_entries(plan, definition, heading_line):
    findings = []
    held = {task.number for task in plan.tasks} if plan.tasks is not None else set()
    for projected in definition.projected:
        rows = [entry for entry in plan.entries if entry.entry == projected]
        if not rows:
            findings.append(Finding("entries", heading_line, "the projected entry `%s` has no "
                                    "row" % projected))
        for entry in rows[1:]:
            findings.append(Finding("entries", entry.line, "the projected entry `%s` has a "
                                    "second row" % projected))
    for entry in plan.entries:
        if entry.entry not in definition.projected:
            findings.append(Finding("entries", entry.line, "`%s` is no projected heading of the "
                                    "definition, word for word" % entry.entry))
        if plan.tasks is not None and plan.numbers_known:
            for column, numbers in (("Realized by", entry.realized or []),
                                    ("Written by", [] if entry.written is None
                                     else [entry.written])):
                for number in numbers:
                    if number not in held:
                        findings.append(Finding("entries", entry.line, "`%s` names task %d, "
                                                "which the plan does not hold"
                                                % (column, number)))
        if entry.realized is not None and entry.written is not None \
                and entry.written not in entry.realized:
            findings.append(Finding("entries", entry.line, "the task that writes the entry, %d, "
                                    "is not among those that realize it" % entry.written))
    return findings


def check_scope(tasks, definition, heading_line):
    findings = []
    named = set()
    for task in tasks:
        for number in task.scope or []:
            named.add(number)
            if number > definition.in_scope:
                findings.append(Finding("scope", task.line, "`In scope` names item %d, while the "
                                        "definition's In scope holds %d items"
                                        % (number, definition.in_scope)))
    if all(task.scope is not None for task in tasks):
        for number in range(1, definition.in_scope + 1):
            if number not in named:
                findings.append(Finding("scope", heading_line, "item %d of the definition's In "
                                        "scope is named by no task" % number))
    return findings


def cycle_through(start, graph):
    """The tasks of a shortest path from `start` back to itself along `Depends on`, or None."""
    paths = {start: [start]}
    queue = [start]
    while queue:
        current = queue.pop(0)
        for following in sorted(graph.get(current, ())):
            if following == start:
                return paths[current] + [start]
            if following not in paths:
                paths[following] = paths[current] + [following]
                queue.append(following)
    return None


def check_dependencies(tasks, numbers_known):
    findings = []
    held = {task.number for task in tasks if task.number is not None}
    graph = {}
    for task in tasks:
        if task.number is not None and task.depends is not None:
            graph.setdefault(task.number, set()).update(n for n in task.depends if n in held)
    for task in tasks:
        if task.depends is None:
            continue
        if numbers_known:
            for number in task.depends:
                if number not in held:
                    findings.append(Finding("dependencies", task.line, "the task depends on task "
                                            "%d, which the plan does not hold" % number))
        if task.number is None:
            continue
        path = cycle_through(task.number, graph)
        if path is not None and len(path) == 2:
            findings.append(Finding("dependencies", task.line, "task %d depends on itself"
                                    % task.number))
        elif path is not None:
            findings.append(Finding("dependencies", task.line, "task %d depends on itself "
                                    "through other tasks: %s" % (task.number,
                                                                 " → ".join(map(str, path)))))
    return findings


def check_preparatory(tasks):
    if any(task.depends is None for task in tasks):
        return []  # a Depends on off its form leaves unknown who depends on what
    findings = []
    for task in tasks:
        if task.preparatory and task.number is not None and not any(
                task.number in other.depends for other in tasks if other is not task):
            findings.append(Finding("preparatory", task.line, "the preparatory task %d has no "
                                    "task depending on it" % task.number))
    return findings


def check_questions(section, definition, tasks, numbers_known):
    findings = []
    held = {task.number for task in tasks} if tasks is not None and numbers_known else None
    lines = [line.strip() for _, line in content(section)]
    found = []
    if lines != ["none"]:
        for number, text in items(section):
            match = PLAN_QUESTION.match(text) if text is not None else None
            if not match:
                findings.append(Finding("questions", number, "the item is none of `- <question> "
                                        "— definition: <place> — plan: task <n>`, `- <question> "
                                        "— definition: <place> — answer: <text>`"))
                continue
            task, answer = match.group("task"), match.group("answer")
            if task is not None and not NUMBER.match(task):
                findings.append(Finding("questions", number, "`plan: task` names no task number"))
                continue
            if task is None and not (answer or "").strip():
                findings.append(Finding("questions", number, "the answer is empty"))
            elif task is not None and held is not None and int(task) not in held:
                findings.append(Finding("questions", number, "the question is sent to task %s, "
                                        "which the plan does not hold" % task))
            found.append((number, match.group("question"), match.group("place")))
    if definition is None:
        return findings
    for question, place in definition.questions:
        standing = [number for number, q, p in found if q == question and p == place]
        if not standing:
            findings.append(Finding("questions", section.heading_line, "the open question `%s` "
                                    "— definition: %s does not stand in the plan word for word"
                                    % (question, place)))
        for number in standing[1:]:
            findings.append(Finding("questions", number, "the open question `%s` stands a second "
                                    "time" % question))
    for number, question, place in found:
        if place != RAISED and (question, place) not in definition.questions:
            findings.append(Finding("questions", number, "the definition holds no open question "
                                    "`%s` resolved in `%s` — a question the breakdown raised reads "
                                    "`definition: none`" % (question, place)))
    return findings


# --- The check --------------------------------------------------------------------------------


def check(plan_text, definition_text, definition_error=None):
    """Return the findings of a plan, sorted by line. `definition_text` is the text of the
    definition the plan names, or None where it could not be read (`definition_error` then says
    why, where known)."""
    preamble, sections = split(plan_text)
    findings, definition = check_header(preamble, definition_text, definition_error)
    section_findings, once = check_sections(sections)
    findings += section_findings
    plan = Plan(once)
    if TASKS in once and content(once[TASKS]):
        table_findings, plan.tasks, plan.numbers_known = read_tasks(once[TASKS])
        findings += table_findings
    if ENTRIES in once and content(once[ENTRIES]):
        table_findings, plan.entries = read_entries(once[ENTRIES], definition)
        findings += table_findings
    if definition is not None and plan.entries is not None:
        findings += check_entries(plan, definition, once[ENTRIES].heading_line)
    if plan.tasks:
        if definition is not None and definition.in_scope is not None:
            findings += check_scope(plan.tasks, definition, once[TASKS].heading_line)
        findings += check_dependencies(plan.tasks, plan.numbers_known)
        findings += check_preparatory(plan.tasks)
    if QUESTIONS in once and content(once[QUESTIONS]):
        findings += check_questions(once[QUESTIONS], definition, plan.tasks, plan.numbers_known)
    return sorted(findings, key=lambda f: f.line)


def read(path):
    """Return (text, None), or (None, why it cannot be read); a path the file system rejects is
    one that cannot be read."""
    try:
        return readiness_check.read(path)
    except ValueError:
        return None, "the file system rejects the path %r" % path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a project plan against its form and "
                                     "against the definition it breaks down.")
    parser.add_argument("plan", help="the project plan, a Markdown file")
    args = parser.parse_args(argv)
    plan_text, error = read(args.plan)
    if error:
        print("error: " + error, file=sys.stderr)
        return 2
    definition_text, definition_error = None, None
    path = definition_path(plan_text)
    if path is not None:
        try:
            full = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(args.plan)),
                                                 path))
            definition_text, definition_error = read(full)
        except ValueError:  # a path the file system rejects, such as one holding NUL
            definition_error = "the file system rejects the path"
    findings = check(plan_text, definition_text, definition_error)
    for finding in findings:
        print(finding)
    print("plan: %s" % ("%d finding(s)" % len(findings) if findings else "nothing found"))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
