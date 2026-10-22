"""Tests of the check of a project plan: every condition fires on a plan broken on purpose, and a
whole plan passes.

Run from the root of the-way:
    python -B gate/run_tests.py project-level

Inputs are written out: a small definition approved at its readiness gate and a whole plan of it.
The expected fingerprint is computed in this file apart from the code under test, by the definition
of WAY-02 as `definition_template.md` applies it: SHA-256 of the UTF-8 text of the definition from
the `## Goal` line up to the `## Gate record` line, that line left out, after every run of spaces
and line breaks becomes one space and both ends are trimmed, its first eight hexadecimal characters.
"""

import contextlib
import hashlib
import io
import os
import re
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_check  # noqa: E402

# --- The definition the plan breaks down -------------------------------------------------------

DEFINITION_SECTIONS = ("Goal", "Background", "In scope", "Out of scope", "Inputs and constraints",
                       "Deliverables", "Success", "Risks", "Open questions",
                       "Touched parts and decisions", "Technology", "Projected foundation changes")

DECISION_HEADING = "(new) — Who can create a player account?"
INVARIANT_HEADING = "player-save-isolation/1"
TERM_HEADING = "mapa"

PROJECTED = """Candidates: 4 shown, 3 accepted — 2026-10-02

### Decisions

#### (new) — Who can create a player account?

Każda osoba z adresem e-mail może założyć jedno konto gracza.

- **Change:** new decision
- **Scope:** accounts
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision
- **Review when:** none
- **Origin:** none
- **Approved by:** Mariusz, 2026-10-03

*Rationale:* gra nie ma jeszcze płatności, więc konto nie musi niczego weryfikować.
*Rejected:* none considered

> **Meaning (pl):** Konto gracza zakłada każdy, kto ma adres e-mail.

### Invariants

#### player-save-isolation/1

Gracz wczytuje tylko zapisy własnego konta.

- **Method:** TODO
- **Rests on:** none
- **Derives from:** TODO — the decision on who can create a player account, projected in this definition
- **Part:** every
- **Correction:** none

> **Meaning (pl):** Gracz nie widzi zapisów innych graczy.

### Glossary

#### mapa

Plansza z siatką heksagonalną, którą gracz przechodzi od startu do wyjścia.

- **Avoid:** poziom
- **Not:** none

> **Meaning (pl):** Mapa to plansza, którą gracz przechodzi od startu do wyjścia."""

QUESTION_BREAKDOWN = "Jak mierzymy postęp gracza?"
QUESTION_EDITOR = "Jakie narzędzia dostaje autor map?"
QUESTION_SAVES = "Gdzie przechowujemy zapisy graczy?"

DEFINITION_BODIES = {
    "Goal": "Gracz przechodzi pierwszą mapę od początku do końca i wraca do zapisanego postępu.",
    "Background": "Gra istnieje tylko jako koncepcja; gracze nie mają jeszcze w co zagrać.",
    "In scope": "- pierwsza mapa na siatce heksagonalnej\n"
                "- zapis postępu gracza\n"
                "- konta graczy\n"
                "- serwer testowy, na którym gra działa",
    "Out of scope": "- edytor map",
    "Inputs and constraints": "- koncepcja projektowa gry",
    "Deliverables": "- grywalna pierwsza mapa na serwerze testowym",
    "Success": "Gracz kończy mapę i wraca do niej po przerwie.\n"
               "**OBALENIE:** jeśli żaden gracz testowy nie kończy mapy — rama jest fałszywa.",
    "Risks": "none",
    "Open questions": "- %s — resolved in: breakdown\n"
                      "- %s — resolved in: task: edytor map\n"
                      "- %s — resolved in: task: konta graczy"
                      % (QUESTION_BREAKDOWN, QUESTION_EDITOR, QUESTION_SAVES),
    "Touched parts and decisions": "none",
    "Technology": "- Język i miejsce działania aplikacji — held by: ARC-01/1",
    "Projected foundation changes": PROJECTED,
}


def body_text(bodies, order):
    return "\n\n".join("## %s\n\n%s" % (name, bodies[name]) for name in order)


def wording_fingerprint(text):
    """WAY-02, written apart from the code under test."""
    normalized = re.sub(r"[ \r\n]+", " ", text).strip(" ")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:8]


def definition_bodies(bodies=None):
    return dict(DEFINITION_BODIES, **(bodies or {}))


def fingerprint_of(bodies=None):
    """The fingerprint of the definition with these bodies: of its text from `## Goal` up to the
    `## Gate record` line, which `definition` below joins to that text by a blank line."""
    return wording_fingerprint(body_text(definition_bodies(bodies), DEFINITION_SECTIONS))


def definition(bodies=None, gate_fingerprint=None, status="Status: approved 2026-10-03"):
    content = body_text(definition_bodies(bodies), DEFINITION_SECTIONS)
    gate = ("- Approved by: Mariusz, 2026-10-03\n"
            "- Foundation searched at: 595f839\n"
            "- Definition fingerprint: %s" % (gate_fingerprint or wording_fingerprint(content)))
    return "# Pierwsza mapa\n\n%s\n\n%s\n\n## Gate record\n\n%s\n" % (status, content, gate)


DEFINITION = definition()
FINGERPRINT = fingerprint_of()
OTHER_FINGERPRINT = "0123abcd" if FINGERPRINT != "0123abcd" else "4567cdef"

# --- The plan ----------------------------------------------------------------------------------

PLAN_SECTIONS = ("Tasks", "Projected entries", "Open questions", "Phases", "Change log")

TASK_COLUMNS = ("#", "Task", "Goal", "Depends on", "In scope", "Preparatory", "State", "Document")
ENTRY_COLUMNS = ("Entry", "Realized by", "Written by")

TASKS = (
    ("1", "test-server", "Serwer testowy przyjmuje wdrożenie gry.", "—", "4", "yes", "to refine",
     "—"),
    ("2", "first-map", "Gracz przechodzi pierwszą mapę na serwerze testowym.", "1", "1", "no",
     "ready for cycle", "[first-map](tasks/first-map.md)"),
    ("3", "player-accounts", "Gracz zakłada konto i po powrocie wczytuje swój postęp.", "1, 2",
     "2, 3", "no", "to refine", "—"),
)

ENTRIES = (
    (DECISION_HEADING, "3", "3"),
    (INVARIANT_HEADING, "2, 3", "3"),
    (TERM_HEADING, "2", "2"),
)

ANSWER_ITEM = ("- %s — definition: breakdown — answer: liczbą ukończonych map "
               "(human, 2026-10-05)" % QUESTION_BREAKDOWN)
EDITOR_ITEM = "- %s — definition: task: edytor map — plan: task 2" % QUESTION_EDITOR
SAVES_ITEM = "- %s — definition: task: konta graczy — plan: task 3" % QUESTION_SAVES
QUESTIONS = "\n".join((ANSWER_ITEM, EDITOR_ITEM, SAVES_ITEM))


def table(columns, rows):
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|" * len(columns)]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def changed(rows, number, column, value, columns=TASK_COLUMNS):
    """The rows with one cell changed: of the row at position `number` (1-based), the column named."""
    result = [list(row) for row in rows]
    result[number - 1][columns.index(column)] = value
    return [tuple(row) for row in result]


def plan(status="Status: draft", definition_line=None, fingerprint=None, tasks=None, entries=None,
         bodies=None, order=None, title="# Plan projektu: Pierwsza mapa"):
    fingerprint = fingerprint or FINGERPRINT
    if definition_line is None:
        definition_line = "Definition: definition.md — fingerprint %s" % fingerprint
    defaults = {
        "Tasks": table(TASK_COLUMNS, TASKS if tasks is None else tasks),
        "Projected entries": table(ENTRY_COLUMNS, ENTRIES if entries is None else entries),
        "Open questions": QUESTIONS,
        "Phases": "none",
        "Change log": "- 2026-10-05 — written from the definition at fingerprint %s" % fingerprint,
    }
    bodies = dict(defaults, **(bodies or {}))
    header = "\n".join(line for line in (status, definition_line) if line)
    return "%s\n\n%s\n\n%s\n" % (title, header, body_text(bodies, order or PLAN_SECTIONS))


PLAN = plan()


def line_of(text, start):
    """The 1-based number of the first line of the text that starts with `start`."""
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith(start):
            return number
    raise AssertionError("no line starts with %r" % start)


def findings(plan_text, definition_text=DEFINITION):
    return plan_check.check(plan_text, definition_text)


def conditions(plan_text, definition_text=DEFINITION):
    return [f.condition for f in findings(plan_text, definition_text)]


# --- Tests -------------------------------------------------------------------------------------


class Whole(unittest.TestCase):
    def test_a_whole_plan_has_no_finding(self):
        self.assertEqual(conditions(PLAN), [])

    def test_a_finding_prints_as_its_line(self):
        found = findings(plan(status="Status: almost done"))
        self.assertTrue(found)
        for finding in found:
            self.assertEqual(str(finding), "fail: %s — line %d: %s"
                             % (finding.condition, finding.line, finding.message))


class Template(unittest.TestCase):
    def template(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plan", "template.md")
        with open(path, encoding="utf-8") as handle:
            return handle.read()

    def test_the_table_headers_the_template_gives_are_the_ones_the_check_reads(self):
        text = self.template()
        form = text.split("\n## The form\n", 1)[1].split("```markdown\n", 1)[1].split("\n```", 1)[0]
        tasks_header = next(line for line in form.splitlines() if line.startswith("| # |"))
        entries_header = next(line for line in form.splitlines() if line.startswith("| Entry |"))
        whole = PLAN.replace(table(TASK_COLUMNS, ()).splitlines()[0], tasks_header)
        whole = whole.replace(table(ENTRY_COLUMNS, ()).splitlines()[0], entries_header)
        self.assertEqual(conditions(whole), [])


class Header(unittest.TestCase):
    def test_a_missing_status_line_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(status="")))

    def test_a_status_off_its_forms_is_reported(self):
        # invariant: project-plan-form
        for status in ("Status: almost done", "Status: handed over", "Status: handed over 5.10.2026",
                       "Status: Draft"):
            with self.subTest(status=status):
                self.assertIn("form", conditions(plan(status=status)))

    def test_a_handed_over_date_that_is_no_calendar_date_is_reported(self):
        # invariant: project-plan-form
        for status in ("Status: handed over 2026-13-45", "Status: handed over 2026-02-30"):
            with self.subTest(status=status):
                self.assertIn("form", conditions(plan(status=status)))

    def test_a_gate_record_without_its_fingerprint_line_is_reported(self):
        # invariant: project-plan-form
        line = "\n- Definition fingerprint: %s" % FINGERPRINT
        self.assertIn(line, DEFINITION)
        self.assertIn("form", conditions(PLAN, DEFINITION.replace(line, "")))

    def in_scope(self, body):
        bodies = {"In scope": body}
        return conditions(plan(fingerprint=fingerprint_of(bodies)), definition(bodies=bodies))

    def test_a_definition_whose_in_scope_holds_no_list_item_is_reported(self):
        # invariant: project-plan-form
        for body in ("Projekt dostarcza pierwszą mapę, zapis postępu, konta i serwer testowy.",
                     "### Gra\n\nPierwsza mapa i zapis postępu."):
            with self.subTest(body=body):
                self.assertIn("form", self.in_scope(body))

    def test_in_scope_items_under_third_level_headings_pass(self):
        body = ("### Gra\n\n"
                "- pierwsza mapa na siatce heksagonalnej\n"
                "- zapis postępu gracza\n"
                "- konta graczy\n\n"
                "### Infrastruktura\n\n"
                "- serwer testowy, na którym gra działa")
        self.assertEqual(self.in_scope(body), [])

    def test_in_scope_with_a_sentence_before_its_list_passes(self):
        self.assertEqual(self.in_scope("Projekt dostarcza:\n\n" + DEFINITION_BODIES["In scope"]),
                         [])

    def test_in_scope_items_written_with_a_star_or_a_plus_pass(self):
        for marker in ("* ", "+ "):
            with self.subTest(marker=marker):
                body = DEFINITION_BODIES["In scope"].replace("- ", marker)
                self.assertEqual(self.in_scope(body), [])

    def test_in_scope_items_numbered_in_order_pass(self):
        for after in (". ", ") "):
            with self.subTest(after=after):
                lines = DEFINITION_BODIES["In scope"].splitlines()
                body = "\n".join("%d%s%s" % (n, after, line[2:])
                                 for n, line in enumerate(lines, start=1))
                self.assertEqual(self.in_scope(body), [])

    def test_a_plan_handed_over_on_a_date_passes(self):
        self.assertEqual(conditions(plan(status="Status: handed over 2026-10-06")), [])

    def test_a_missing_definition_line_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(definition_line="")))

    def test_a_definition_line_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for line in ("Definition: definition.md",
                     "Definition: definition.md — fingerprint %s" % FINGERPRINT[:7],
                     "Definition: definition.md — fingerprint %sz" % FINGERPRINT[:7],
                     "Definition: — fingerprint %s" % FINGERPRINT):
            with self.subTest(line=line):
                self.assertIn("form", conditions(plan(definition_line=line)))

    def test_a_fingerprint_in_capitals_is_reported(self):
        # invariant: project-plan-form
        line = "Definition: definition.md — fingerprint ABCDEF12"
        self.assertIn("form", conditions(plan(definition_line=line)))

    def test_a_definition_that_cannot_be_read_is_reported(self):
        # invariant: project-plan-form
        self.assertEqual(set(conditions(PLAN, None)), {"form"})

    def test_a_fingerprint_matching_the_gate_record_but_not_the_changed_definition_is_reported(self):
        # invariant: project-plan-form
        changed_after_gate = DEFINITION.replace("- edytor map", "- edytor map\n- tryb wieloosobowy")
        self.assertNotEqual(changed_after_gate, DEFINITION)
        self.assertIn("- Definition fingerprint: %s" % FINGERPRINT, changed_after_gate)
        self.assertIn("form", conditions(PLAN, changed_after_gate))

    def test_a_fingerprint_other_than_the_one_the_gate_record_and_the_text_hold_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(fingerprint=OTHER_FINGERPRINT)))

    def test_a_fingerprint_matching_the_text_but_not_the_gate_record_is_reported(self):
        # invariant: project-plan-form
        stale_gate = definition(gate_fingerprint=OTHER_FINGERPRINT)
        self.assertIn("form", conditions(PLAN, stale_gate))

    def test_a_change_of_spaces_in_the_definition_keeps_the_fingerprint(self):
        respaced = DEFINITION.replace("Gra istnieje tylko jako koncepcja;",
                                      "Gra istnieje  tylko\njako koncepcja;")
        self.assertEqual(conditions(PLAN, respaced), [])


class Sections(unittest.TestCase):
    def test_a_missing_section_is_reported(self):
        # invariant: project-plan-form
        order = [name for name in PLAN_SECTIONS if name != "Phases"]
        self.assertIn("form", conditions(plan(order=order)))

    def test_a_section_standing_twice_is_reported(self):
        # invariant: project-plan-form
        order = list(PLAN_SECTIONS) + ["Phases"]
        self.assertIn("form", conditions(plan(order=order)))

    def test_a_section_outside_the_template_is_reported(self):
        # invariant: project-plan-form
        text = PLAN.replace("## Phases", "## Notes\n\nPlan pisany razem z Mariuszem.\n\n## Phases")
        self.assertIn("form", conditions(text))

    def test_sections_out_of_order_are_reported(self):
        # invariant: project-plan-form
        order = ["Tasks", "Projected entries", "Phases", "Open questions", "Change log"]
        self.assertIn("form", conditions(plan(order=order)))

    def test_a_heading_inside_a_fenced_block_is_no_section(self):
        phases = ("- Faza 1: zadania 1, 2 — zamyka ją wdrożenie mapy na serwer testowy\n\n"
                  "```\n## Not a section\n```")
        self.assertEqual(conditions(plan(bodies={"Phases": phases})), [])

    def test_an_empty_section_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(bodies={"Phases": ""})))

    def test_a_change_log_without_a_dated_item_is_reported(self):
        # invariant: project-plan-form
        for log in ("- written from the definition at fingerprint %s" % FINGERPRINT,
                    "Plan napisany z definicji.", "none"):
            with self.subTest(log=log):
                self.assertIn("form", conditions(plan(bodies={"Change log": log})))

    def test_a_tasks_section_without_its_table_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(bodies={"Tasks": "none"})))

    def test_a_projected_entries_section_without_its_table_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(bodies={"Projected entries": "TODO"})))

    def test_projected_entries_reading_none_while_the_definition_projects_entries_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(bodies={"Projected entries": "none"})))

    def test_a_definition_projecting_no_entry_lets_projected_entries_read_none(self):
        bodies = {"Projected foundation changes": "Candidates: 2 shown, 0 accepted — 2026-10-02"
                                                  "\n\nnone"}
        text = definition(bodies=bodies)
        found = conditions(plan(fingerprint=fingerprint_of(bodies),
                                bodies={"Projected entries": "none"}), text)
        self.assertEqual(found, [])


class TasksTable(unittest.TestCase):
    def test_a_tasks_header_off_the_template_is_reported(self):
        # invariant: project-plan-form
        header = table(TASK_COLUMNS, ()).splitlines()[0]
        for other in (header.replace(" Depends on |", " Depends |"),
                      header.replace(" Document |", ""),
                      header.replace("| Goal | Depends on |", "| Depends on | Goal |")):
            with self.subTest(header=other):
                self.assertIn("form", conditions(PLAN.replace(header, other)))

    def test_a_tasks_table_without_a_task_row_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(tasks=())))

    def test_a_task_number_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for value in ("0", "a", "-1", "1.", ""):
            with self.subTest(value=value):
                tasks = changed(TASKS, 1, "#", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_task_name_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for value in ("Test-Server", "test_server", "test--server", "-test-server",
                      "test-server-", "test server", ""):
            with self.subTest(value=value):
                tasks = changed(TASKS, 1, "Task", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_task_name_with_digits_passes(self):
        tasks = changed(TASKS, 2, "Task", "first-map-2")
        self.assertEqual(conditions(plan(tasks=tasks)), [])

    def test_an_empty_goal_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(tasks=changed(TASKS, 2, "Goal", ""))))

    def test_depends_on_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for value in ("1,2", "1 2", "1 i 2", "", "-", "0"):
            with self.subTest(value=value):
                tasks = changed(TASKS, 3, "Depends on", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_in_scope_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for value in ("2,3", "2 i 3", "", "zapis postępu"):
            with self.subTest(value=value):
                tasks = changed(TASKS, 3, "In scope", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_preparatory_off_its_form_is_reported(self):
        # invariant: project-plan-form
        for value in ("tak", "Yes", ""):
            with self.subTest(value=value):
                tasks = changed(TASKS, 1, "Preparatory", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_state_off_the_list_is_reported_at_its_row(self):
        # invariant: project-plan-form
        text = plan(tasks=changed(TASKS, 3, "State", "blocked"))
        row = line_of(text, "| 3 | player-accounts |")
        self.assertIn(("form", row), [(f.condition, f.line) for f in findings(text)])

    def test_states_off_the_list_are_reported(self):
        # invariant: project-plan-form
        for value in ("To refine", "done — goal delivered in task", "dropped",
                      "done — goal delivered in task x", ""):
            with self.subTest(value=value):
                tasks = changed(TASKS, 3, "State", value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_goal_delivered_in_a_task_the_plan_does_not_hold_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 2, "State", "done — goal delivered in task 9")
        self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_goal_delivered_in_the_task_itself_is_reported(self):
        # invariant: project-plan-form
        tasks = changed(TASKS, 2, "State", "done — goal delivered in task 2")
        self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_task_row_with_an_extra_cell_is_reported(self):
        # invariant: project-plan-form
        rows = list(TASKS)
        rows[1] = rows[1] + ("uwaga",)
        self.assertIn("form", conditions(plan(tasks=rows)))

    def test_a_separator_row_whose_cell_count_differs_from_the_header_is_reported(self):
        # invariant: project-plan-form
        separator = "|" + "---|" * len(TASK_COLUMNS)
        self.assertIn(separator, PLAN)
        text = PLAN.replace(separator, "|" + "---|" * (len(TASK_COLUMNS) - 1), 1)
        self.assertIn("form", conditions(text))

    def test_a_number_in_digits_other_than_ascii_is_reported(self):
        # invariant: project-plan-form
        for column, value in (("Depends on", "1, ２"), ("In scope", "2, ٣"),
                              ("#", "３")):
            with self.subTest(column=column, value=value):
                tasks = changed(TASKS, 3, column, value)
                self.assertIn("form", conditions(plan(tasks=tasks)))

    # A task 23 the plan holds, so that a digit read as a number would name a task that exists.
    TASK_23 = ("23", "map-tutorial", "Gracz przechodzi samouczek przed pierwszą mapą.", "2", "1",
               "no", "to refine", "—")

    def test_a_task_number_with_an_arabic_indic_digit_is_reported(self):
        # invariant: project-plan-form
        # Read as 33, `3٣` would be a fresh number and the plan would pass.
        fourth = ("3٣", "map-tutorial", "Gracz przechodzi samouczek przed pierwszą mapą.",
                  "2", "1", "no", "to refine", "—")
        self.assertIn("form", conditions(plan(tasks=list(TASKS) + [fourth])))

    def test_depends_on_with_an_arabic_indic_digit_is_reported(self):
        # invariant: project-plan-form
        # Read as 23, `2٣` would name the task 23 the plan holds and the plan would pass.
        tasks = changed(list(TASKS) + [self.TASK_23], 3, "Depends on", "1, 2٣")
        self.assertEqual(conditions(plan(tasks=changed(tasks, 3, "Depends on", "1, 23"))), [])
        self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_goal_delivered_in_a_task_written_with_an_arabic_indic_digit_is_reported(self):
        # invariant: project-plan-form
        # Read as 23, `2٣` would name the task 23 the plan holds and the plan would pass.
        tasks = list(TASKS) + [self.TASK_23]
        self.assertEqual(conditions(plan(tasks=changed(
            tasks, 3, "State", "done — goal delivered in task 23"))), [])
        tasks = changed(tasks, 3, "State", "done — goal delivered in task 2٣")
        self.assertIn("form", conditions(plan(tasks=tasks)))

    def test_a_change_log_item_dated_in_arabic_indic_digits_is_reported(self):
        log = "- ٢٠٢٦-١٠-٠٥ — written"
        self.assertIn("form", conditions(plan(bodies={"Change log": log})))

    def test_every_state_of_the_list_passes(self):
        for value in ("to refine", "waiting for human", "ready for cycle", "in cycle", "done",
                      "done — goal delivered in task 2", "dropped — approved by human"):
            with self.subTest(value=value):
                tasks = changed(TASKS, 3, "State", value)
                self.assertEqual(conditions(plan(tasks=tasks)), [])

    def test_an_empty_document_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(tasks=changed(TASKS, 2, "Document", ""))))

    def test_a_number_held_by_two_tasks_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(tasks=changed(TASKS, 3, "#", "2"))))

    def test_a_name_held_by_two_tasks_is_reported(self):
        # invariant: project-plan-form
        self.assertIn("form", conditions(plan(tasks=changed(TASKS, 3, "Task", "first-map"))))


class EntriesTable(unittest.TestCase):
    def test_an_entries_header_off_the_template_is_reported(self):
        # invariant: project-plan-form
        header = table(ENTRY_COLUMNS, ()).splitlines()[0]
        for other in ("| Entry | Realized by |", "| Entry | Written by | Realized by |",
                      "| Projected entry | Realized by | Written by |"):
            with self.subTest(header=other):
                self.assertIn("form", conditions(PLAN.replace(header, other)))

    def test_realized_by_off_its_form_is_reported(self):
        # invariant: project-plan-form
        # invariant: project-plan-check
        for value in ("2,3", "2 i 3", "", "—"):
            with self.subTest(value=value):
                entries = changed(ENTRIES, 2, "Realized by", value, ENTRY_COLUMNS)
                self.assertIn("form", conditions(plan(entries=entries)))

    def test_written_by_naming_two_tasks_is_reported(self):
        # invariant: project-plan-form
        # invariant: project-plan-check
        entries = changed(ENTRIES, 2, "Written by", "2, 3", ENTRY_COLUMNS)
        self.assertIn("form", conditions(plan(entries=entries)))

    def test_written_by_empty_or_off_its_form_is_reported(self):
        # invariant: project-plan-form
        # invariant: project-plan-check
        for value in ("", "—", "task 3"):
            with self.subTest(value=value):
                entries = changed(ENTRIES, 2, "Written by", value, ENTRY_COLUMNS)
                self.assertIn("form", conditions(plan(entries=entries)))


class Entries(unittest.TestCase):
    def test_a_projected_heading_with_no_row_is_reported(self):
        # invariant: project-plan-check
        entries = [row for row in ENTRIES if row[0] != TERM_HEADING]
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_two_rows_for_one_projected_heading_are_reported(self):
        # invariant: project-plan-check
        entries = list(ENTRIES) + [(TERM_HEADING, "3", "3")]
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_a_row_that_is_no_projected_heading_is_reported_at_its_row(self):
        # invariant: project-plan-check
        entries = list(ENTRIES) + [("(new) — Who keeps the map?", "2", "2")]
        text = plan(entries=entries)
        row = line_of(text, "| (new) — Who keeps the map? |")
        found = [(f.condition, f.line) for f in findings(text)]
        self.assertEqual(found, [("entries", row)])

    def test_a_row_naming_the_entry_with_one_word_changed_is_reported(self):
        # invariant: project-plan-check
        entries = changed(ENTRIES, 1, "Entry", "(new) — Who may create a player account?",
                          ENTRY_COLUMNS)
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_a_row_naming_the_invariant_without_its_version_is_reported(self):
        # invariant: project-plan-check
        entries = changed(ENTRIES, 2, "Entry", "player-save-isolation", ENTRY_COLUMNS)
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_realized_by_naming_a_task_the_plan_does_not_hold_is_reported(self):
        # invariant: project-plan-check
        entries = changed(ENTRIES, 3, "Realized by", "2, 9", ENTRY_COLUMNS)
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_written_by_naming_a_task_the_plan_does_not_hold_is_reported(self):
        # invariant: project-plan-check
        entries = changed(ENTRIES, 3, "Written by", "9", ENTRY_COLUMNS)
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_written_by_a_task_not_among_realized_by_is_reported(self):
        # invariant: project-plan-check
        entries = changed(ENTRIES, 2, "Realized by", "2", ENTRY_COLUMNS)
        self.assertEqual(set(conditions(plan(entries=entries))), {"entries"})

    def test_a_projected_heading_holding_a_bar_written_escaped_in_its_cell_passes(self):
        bodies = {"Projected foundation changes": PROJECTED.replace(
            "#### mapa\n", "#### mapa | plansza\n")}
        text = definition(bodies=bodies)
        self.assertIn("#### mapa | plansza\n", text)
        entries = changed(ENTRIES, 3, "Entry", "mapa \\| plansza", ENTRY_COLUMNS)
        found = conditions(plan(entries=entries, fingerprint=fingerprint_of(bodies)), text)
        self.assertEqual(found, [])

    def test_a_level_four_heading_outside_projected_changes_is_no_projected_entry(self):
        bodies = {"Background": "Gra istnieje tylko jako koncepcja.\n\n"
                                "#### (new) — Who keeps the map?"}
        text = definition(bodies=bodies)
        self.assertEqual(conditions(plan(fingerprint=fingerprint_of(bodies)), text), [])


class Scope(unittest.TestCase):
    def test_an_in_scope_item_no_task_names_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 3, "In scope", "2")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"scope"})

    def test_an_in_scope_number_above_the_count_of_items_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 3, "In scope", "2, 3, 5")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"scope"})

    def test_an_item_named_by_two_tasks_passes(self):
        tasks = changed(TASKS, 3, "In scope", "1, 2, 3")
        self.assertEqual(conditions(plan(tasks=tasks)), [])

    def test_a_nested_detail_under_an_in_scope_item_is_no_item(self):
        bodies = {"In scope": DEFINITION_BODIES["In scope"].replace(
            "- konta graczy", "- konta graczy\n  - logowanie adresem e-mail")}
        text = definition(bodies=bodies)
        self.assertEqual(conditions(plan(fingerprint=fingerprint_of(bodies)), text), [])

    def test_a_number_naming_a_nested_detail_is_above_the_count(self):
        # invariant: project-plan-check
        bodies = {"In scope": DEFINITION_BODIES["In scope"].replace(
            "- konta graczy", "- konta graczy\n  - logowanie adresem e-mail")}
        text = definition(bodies=bodies)
        tasks = changed(TASKS, 3, "In scope", "2, 3, 5")
        self.assertEqual(set(conditions(plan(tasks=tasks, fingerprint=fingerprint_of(bodies)),
                                        text)), {"scope"})


    FENCED = DEFINITION_BODIES["In scope"] + "\n\n```\n- przykład\n```"

    def with_in_scope(self, body, tasks=None):
        bodies = {"In scope": body}
        return conditions(plan(tasks=tasks, fingerprint=fingerprint_of(bodies)),
                          definition(bodies=bodies))

    def test_a_number_naming_a_line_in_a_fenced_block_is_above_the_count(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 3, "In scope", "2, 3, 5")
        self.assertEqual(set(self.with_in_scope(self.FENCED, tasks)), {"scope"})

    def test_a_fenced_block_after_the_in_scope_items_is_no_item(self):
        self.assertEqual(self.with_in_scope(self.FENCED), [])

    def test_an_item_whose_marker_is_followed_by_a_tab_counts(self):
        body = DEFINITION_BODIES["In scope"].replace("- konta graczy", "-\tkonta graczy")
        self.assertIn("-\tkonta graczy", body)
        self.assertEqual(self.with_in_scope(body), [])

    def test_a_horizontal_rule_after_the_in_scope_items_is_no_item(self):
        for rule in ("- - -", "* * *"):
            with self.subTest(rule=rule):
                body = DEFINITION_BODIES["In scope"] + "\n\n" + rule
                self.assertEqual(self.with_in_scope(body), [])


class Dependencies(unittest.TestCase):
    def test_a_task_depending_on_a_number_the_plan_does_not_hold_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 3, "Depends on", "1, 2, 7")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"dependencies"})

    def test_a_task_depending_on_itself_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 2, "Depends on", "1, 2")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"dependencies"})

    def test_a_cycle_through_two_tasks_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 2, "Depends on", "1, 3")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"dependencies"})

    def test_a_cycle_through_three_tasks_is_reported(self):
        # invariant: project-plan-check
        # 1 needs 3, 3 needs 2, 2 needs 1: no two of them depend on each other directly.
        tasks = changed(changed(TASKS, 1, "Depends on", "3"), 3, "Depends on", "2")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"dependencies"})

    def test_tasks_with_no_dependency_pass(self):
        tasks = changed(changed(TASKS, 1, "Preparatory", "no"), 3, "Depends on", "—")
        tasks = changed(tasks, 2, "Depends on", "—")
        self.assertEqual(conditions(plan(tasks=tasks)), [])


class Preparatory(unittest.TestCase):
    def test_a_preparatory_task_no_task_depends_on_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(changed(TASKS, 2, "Depends on", "—"), 3, "Depends on", "2")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"preparatory"})

    def test_a_preparatory_task_at_the_end_of_the_plan_is_reported(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 3, "Preparatory", "yes")
        self.assertEqual(set(conditions(plan(tasks=tasks))), {"preparatory"})

    def test_a_preparatory_task_one_task_depends_on_passes(self):
        tasks = changed(TASKS, 3, "Depends on", "2")
        self.assertEqual(conditions(plan(tasks=tasks)), [])


class Questions(unittest.TestCase):
    def questions(self, body, definition_text=DEFINITION, fingerprint=None):
        return conditions(plan(bodies={"Open questions": body}, fingerprint=fingerprint),
                          definition_text)

    def test_an_open_question_missing_from_the_plan_is_reported(self):
        # invariant: project-plan-check
        body = "\n".join((ANSWER_ITEM, EDITOR_ITEM))
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_an_open_question_reworded_by_one_word_is_reported(self):
        # invariant: project-plan-check
        body = QUESTIONS.replace("Jak mierzymy postęp gracza?", "Jak liczymy postęp gracza?")
        self.assertNotEqual(body, QUESTIONS)
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_a_place_of_the_definition_reworded_is_reported(self):
        # invariant: project-plan-check
        body = QUESTIONS.replace("— definition: task: edytor map —", "— definition: task: edytor —")
        self.assertNotEqual(body, QUESTIONS)
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_a_question_sent_to_a_task_the_plan_does_not_hold_is_reported(self):
        # invariant: project-plan-check
        body = QUESTIONS.replace("— plan: task 3", "— plan: task 9")
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_an_empty_answer_is_reported(self):
        # invariant: project-plan-check
        empty = "- %s — definition: breakdown — answer: " % QUESTION_BREAKDOWN
        body = "\n".join((empty, EDITOR_ITEM, SAVES_ITEM))
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_an_item_of_none_of_the_forms_is_reported_at_its_line(self):
        # invariant: project-plan-check
        odd = "- %s — breakdown" % QUESTION_BREAKDOWN
        body = "\n".join((ANSWER_ITEM, EDITOR_ITEM, SAVES_ITEM, odd))
        text = plan(bodies={"Open questions": body})
        found = [(f.condition, f.line) for f in findings(text)]
        self.assertIn(("questions", line_of(text, odd)), found)
        self.assertEqual({c for c, _ in found}, {"questions"})

    def test_a_question_the_definition_does_not_hold_with_a_place_of_it_is_reported(self):
        # invariant: project-plan-check
        extra = "- Czy gra ma tryb nocny? — definition: breakdown — plan: task 2"
        body = "\n".join((ANSWER_ITEM, EDITOR_ITEM, SAVES_ITEM, extra))
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_an_open_question_standing_as_two_items_is_reported(self):
        # invariant: project-plan-check
        twice = SAVES_ITEM.replace("— plan: task 3", "— plan: task 2")
        body = "\n".join((ANSWER_ITEM, EDITOR_ITEM, SAVES_ITEM, twice))
        self.assertEqual(set(self.questions(body)), {"questions"})

    def test_a_plan_reading_none_while_the_definition_holds_questions_is_reported(self):
        # invariant: project-plan-check
        self.assertEqual(set(self.questions("none")), {"questions"})

    def test_a_question_the_breakdown_raised_passes(self):
        for raised in ("- Czy gra ma tryb nocny? — definition: none — plan: task 2",
                       "- Czy gra ma tryb nocny? — definition: none — answer: nie "
                       "(human, 2026-10-05)"):
            with self.subTest(raised=raised):
                body = "\n".join((ANSWER_ITEM, EDITOR_ITEM, SAVES_ITEM, raised))
                self.assertEqual(self.questions(body), [])

    def test_a_question_moved_to_another_task_is_no_finding_of_the_script(self):
        # Whether the change log gives the reason for the move is the critique's to judge.
        body = QUESTIONS.replace(SAVES_ITEM, SAVES_ITEM.replace("— plan: task 3", "— plan: task 2"))
        self.assertNotEqual(body, QUESTIONS)
        self.assertEqual(self.questions(body), [])

    def test_a_breakdown_question_sent_to_a_task_is_no_finding_of_the_script(self):
        moved = "- %s — definition: breakdown — plan: task 3" % QUESTION_BREAKDOWN
        body = QUESTIONS.replace(ANSWER_ITEM, moved)
        self.assertEqual(self.questions(body), [])

    def test_a_task_question_answered_in_the_plan_passes(self):
        answered = ("- %s — definition: task: edytor map — answer: edytor jest poza zakresem "
                    "(definition.md, Out of scope)" % QUESTION_EDITOR)
        body = QUESTIONS.replace(EDITOR_ITEM, answered)
        self.assertEqual(self.questions(body), [])

    def test_a_definition_with_no_questions_lets_the_plan_read_none(self):
        bodies = {"Open questions": "none"}
        text = definition(bodies=bodies)
        self.assertEqual(self.questions("none", text, fingerprint_of(bodies)), [])


class Command(unittest.TestCase):
    def call(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = plan_check.main(argv)
            except SystemExit as exit_:
                code = exit_.code
        return code, out.getvalue(), err.getvalue()

    def run_main(self, plan_text, definition_text=DEFINITION, encoding="utf-8",
                 definition_encoding="utf-8", plan_name="plan.md",
                 definition_name="definition.md"):
        with tempfile.TemporaryDirectory() as directory:
            plan_path = os.path.join(directory, plan_name)
            os.makedirs(os.path.dirname(plan_path), exist_ok=True)
            with open(plan_path, "w", encoding=encoding, newline="") as handle:
                handle.write(plan_text)
            if definition_text is not None:
                path = os.path.join(directory, definition_name)
                with open(path, "w", encoding=definition_encoding, newline="") as handle:
                    handle.write(definition_text)
            return self.call([plan_path])

    def assert_findings_printed(self, out):
        lines = out.splitlines()
        self.assertTrue(lines)
        fails, last = lines[:-1], lines[-1]
        self.assertTrue(fails)
        for line in fails:
            self.assertRegex(line, r"^fail: [a-z]+ — line \d+: \S")
        self.assertEqual(last, "plan: %d finding(s)" % len(fails))
        return [(re.match(r"^fail: ([a-z]+) — line (\d+):", line).group(1),
                 int(re.match(r"^fail: ([a-z]+) — line (\d+):", line).group(2))) for line in fails]

    def test_a_whole_plan_exits_zero(self):
        code, out, _ = self.run_main(PLAN)
        self.assertEqual((code, out), (0, "plan: nothing found\n"))

    def test_findings_exit_one_and_print_sorted_by_line(self):
        # invariant: project-plan-check
        tasks = changed(TASKS, 2, "In scope", "1, 7")
        entries = list(ENTRIES) + [("(new) — Who keeps the map?", "2", "2")]
        extra = "- Czy gra ma tryb nocny? — definition: breakdown — plan: task 2"
        text = plan(tasks=tasks, entries=entries,
                    bodies={"Open questions": "\n".join((QUESTIONS, extra))})
        code, out, _ = self.run_main(text)
        self.assertEqual(code, 1)
        printed = self.assert_findings_printed(out)
        self.assertEqual(len(printed), 3)
        self.assertEqual({c for c, _ in printed}, {"scope", "entries", "questions"})
        numbers = [n for _, n in printed]
        self.assertEqual(numbers, sorted(numbers))

    def test_a_missing_plan_exits_two(self):
        code, _, err = self.call([os.path.join(tempfile.gettempdir(), "no-such-plan.md")])
        self.assertEqual(code, 2)
        self.assertTrue(err.startswith("error: "), err)

    def test_a_plan_that_is_not_utf_8_exits_two(self):
        code, _, err = self.run_main(PLAN, encoding="cp1250")
        self.assertEqual(code, 2)
        self.assertTrue(err.startswith("error: "), err)

    def test_a_call_without_a_plan_exits_two(self):
        code, _, _ = self.call([])
        self.assertEqual(code, 2)

    def test_a_missing_definition_is_a_form_finding(self):
        # invariant: project-plan-form
        code, out, _ = self.run_main(PLAN, definition_text=None)
        self.assertEqual(code, 1)
        self.assertEqual({c for c, _ in self.assert_findings_printed(out)}, {"form"})

    def test_a_definition_that_is_not_utf_8_is_a_form_finding(self):
        # invariant: project-plan-form
        code, out, _ = self.run_main(PLAN, definition_encoding="cp1250")
        self.assertEqual(code, 1)
        self.assertEqual({c for c, _ in self.assert_findings_printed(out)}, {"form"})

    def test_a_definition_file_that_is_no_project_definition_is_a_form_finding(self):
        # invariant: project-plan-form
        note = "# Notatka o mapie\n\nKilka myśli o pierwszej mapie i o tym, kto w nią zagra.\n"
        code, out, _ = self.run_main(PLAN, definition_text=note)
        self.assertEqual(code, 1)
        self.assertIn("form", {c for c, _ in self.assert_findings_printed(out)})

    def test_a_definition_path_the_file_system_rejects_is_a_form_finding(self):
        # invariant: project-plan-form
        text = plan(definition_line="Definition: defi\x00nition.md — fingerprint %s" % FINGERPRINT)
        code, out, _ = self.run_main(text)
        self.assertEqual(code, 1)
        self.assertIn("form", {c for c, _ in self.assert_findings_printed(out)})

    def test_the_definition_is_read_by_its_path_relative_to_the_plan(self):
        text = plan(definition_line="Definition: ../definition.md — fingerprint %s" % FINGERPRINT)
        code, out, _ = self.run_main(text, plan_name=os.path.join("plans", "plan.md"))
        self.assertEqual((code, out), (0, "plan: nothing found\n"))

    def test_a_crlf_plan_and_definition_pass(self):
        code, out, _ = self.run_main(PLAN.replace("\n", "\r\n"), DEFINITION.replace("\n", "\r\n"))
        self.assertEqual((code, out), (0, "plan: nothing found\n"))


if __name__ == "__main__":
    unittest.main()
