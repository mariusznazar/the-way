"""Tests of the readiness check of a project definition: every condition fires on a definition
broken on purpose, and a whole definition passes.

Run from the root of the-way:
    python -B gate/run_tests.py project-level

Inputs are written out. The expected fingerprint is computed in this file apart from the code
under test, by the definition of WAY-02: SHA-256 of the UTF-8 text after every run of spaces and
line breaks becomes one space and both ends are trimmed, its first eight hexadecimal characters.
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
import readiness_check  # noqa: E402

DECISION = """#### (new) — What does the archive exclude for good?

The archive has no public write API.

- **Scope:** archive
- **Based on:** none
- **Relations:** none
- **Verification:** an agent compares the change with the decision
- **Origin:** none

*Rationale:* publishing is outside the archive's purpose.
*Rejected:* none considered

> **Meaning (pl):** Archiwum nie udostępnia publicznego interfejsu zapisu."""

INVARIANT = """#### one-workspace-per-document

Every document belongs to exactly one workspace.

- **Method:** review
- **Rests on:** TODO — the store of documents, once a task chooses it
- **Derives from:** TODO — the decision on who owns a document, projected in this definition
- **Part:** every
- **Violated:** no

> **Meaning (pl):** TODO"""

CANDIDATES_LINE = "Candidates: 3 shown, 1 accepted — 2026-10-03"


def projected(entries=None, first=CANDIDATES_LINE):
    """The section of projected foundation changes: its candidates line, then its entries."""
    if entries is None:
        entries = "### Decisions\n\n" + DECISION
    return "%s\n\n%s" % (first, entries)


BODIES = {
    "Goal": "Gracz przechodzi pierwszą mapę od początku do końca.",
    "Background": "Gra istnieje tylko jako koncepcja.",
    "In scope": "- pierwsza mapa\n- zapis postępu",
    "Out of scope": "- edytor map",
    "Inputs and constraints": "- koncepcja projektowa",
    "Deliverables": "- grywalna pierwsza mapa",
    "Success": "Gracz kończy mapę.\n**OBALENIE:** jeśli nikt nie kończy mapy — rama jest fałszywa.",
    "Risks": "none",
    "Open questions": "- Jak mierzymy postęp? — resolved in: breakdown\n"
                      "- Jakie narzędzia ma autor? — resolved in: task: edytor",
    "Touched parts and decisions": "none",
    "Technology": "- Język i miejsce działania aplikacji — held by: ARC-01",
    "Projected foundation changes": projected(),
}


def body_text(bodies, order):
    return "\n\n".join("## %s\n\n%s" % (name, bodies[name]) for name in order)


def wording_fingerprint(text):
    """WAY-02, written apart from the code under test."""
    normalized = re.sub(r"[ \r\n]+", " ", text).strip(" ")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:8]


def definition(status="Status: approved 2026-10-03", bodies=None, gate=None, order=None,
               fingerprint=None):
    bodies = dict(BODIES, **(bodies or {}))
    order = order or list(readiness_check.SECTIONS[:-1])
    content = body_text(bodies, order)
    if gate is None:
        gate = ("- Approved by: Mariusz, 2026-10-03\n"
                "- Foundation searched at: 595f839\n"
                "- Definition fingerprint: %s" % (fingerprint or wording_fingerprint(content)))
    return "# Pierwsza mapa\n\n%s\n\n%s\n\n## Gate record\n\n%s\n" % (status, content, gate)


def conditions(text, before_approval=False):
    return [(f.condition, f.message) for f in readiness_check.check(text, before_approval)]


class Template(unittest.TestCase):
    def template(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "definition_template.md")
        with open(path, encoding="utf-8") as handle:
            return handle.read()

    def test_the_form_the_template_gives_has_the_structure_the_check_reads(self):
        text = self.template()
        form = text.split("\n## The form\n", 1)[1].split("```markdown\n", 1)[1].split("\n```", 1)[0]
        self.assertEqual(readiness_check.check_structure(*readiness_check.split(form)), [])

    def test_the_projected_section_the_template_gives_passes_its_checks(self):
        text = self.template()
        marker = "```markdown\n## Projected foundation changes\n"
        block = "## Projected foundation changes\n" + text.split(marker, 1)[1].split("\n```", 1)[0]
        _, sections = readiness_check.split(block)
        self.assertEqual(readiness_check.check_candidates(sections[0]), [])
        self.assertEqual(readiness_check.check_gaps(sections), [])

    def test_the_technology_section_the_template_gives_passes_its_checks(self):
        text = self.template()
        technology = ("## Technology\n" +
                      text.split("```markdown\n## Technology\n", 1)[1].split("\n```", 1)[0])
        marker = "```markdown\n## Projected foundation changes\n"
        block = ("## Projected foundation changes\n" +
                 text.split(marker, 1)[1].split("\n```", 1)[0])
        _, sections = readiness_check.split(technology + "\n" + block)
        self.assertEqual(readiness_check.check_technology(sections[0], sections[1]), [])

    def test_the_working_table_the_template_gives_is_the_one_the_check_reads(self):
        self.assertIn("```markdown\n%s\n" % readiness_check.WORKING_TABLE, self.template())


class Whole(unittest.TestCase):
    def test_a_whole_approved_definition_has_no_finding(self):
        self.assertEqual(conditions(definition()), [])

    def test_a_definition_waiting_for_approval_passes_before_approval(self):
        text = definition(status="Status: ready for gate", gate="")
        self.assertEqual(conditions(text, before_approval=True), [])


class Structure(unittest.TestCase):
    def test_a_missing_status_line_is_reported(self):
        # invariant: project-definition-form
        self.assertEqual(conditions(definition(status="")),
                         [("structure", "no `Status:` line above the first section")])

    def test_a_status_off_its_forms_is_reported(self):
        # invariant: project-definition-form
        found = conditions(definition(status="Status: almost done"))
        self.assertEqual([c for c, _ in found], ["structure"])

    def test_a_missing_section_is_reported(self):
        # invariant: project-definition-form
        order = [n for n in readiness_check.SECTIONS[:-1] if n != "Risks"]
        found = conditions(definition(order=order))
        self.assertIn(("structure", "the section `## Risks` is missing"), found)

    def test_a_section_standing_twice_is_reported(self):
        # invariant: project-definition-form
        order = list(readiness_check.SECTIONS[:-1]) + ["Risks"]
        found = conditions(definition(order=order))
        self.assertIn(("structure", "`## Risks` stands a second time"), found)

    def test_a_section_outside_the_template_is_reported(self):
        # invariant: project-definition-form
        text = definition().replace("## Risks", "## Stakeholders\n\nMariusz\n\n## Risks")
        self.assertIn(("structure", "`## Stakeholders` is no section of the template"),
                      conditions(text))

    def test_sections_out_of_order_are_reported(self):
        # invariant: project-definition-form
        order = list(readiness_check.SECTIONS[:-1])
        order[0], order[1] = order[1], order[0]
        found = conditions(definition(order=order))
        self.assertEqual([c for c, _ in found], ["structure"])

    def test_a_heading_inside_a_fenced_block_is_no_section(self):
        text = definition(bodies={"Background": "```\n## Not a section\n```"})
        self.assertEqual(conditions(text), [])

    def test_a_yaml_front_matter_above_the_title_is_no_obstacle(self):
        text = "---\ntitle: Pierwsza mapa\nstatus: draft\n---\n\n" + definition()
        self.assertEqual(conditions(text), [])

    def test_a_third_level_heading_is_no_section(self):
        text = definition(bodies={"Background": "### A detail\n\nGra istnieje tylko jako koncepcja."})
        self.assertEqual(conditions(text), [])


class Gaps(unittest.TestCase):
    def test_todo_in_a_section_is_reported_with_its_line(self):
        # invariant: project-readiness-gate
        text = definition(bodies={"Success": "TODO"})
        findings = readiness_check.check(text)
        todo = [f for f in findings if f.condition == "a"]
        self.assertEqual(len(todo), 1)
        self.assertEqual(text.splitlines()[todo[0].line - 1], "TODO")

    def test_todo_in_a_field_waiting_for_code_is_no_gap(self):
        decision = DECISION.replace(
            "- **Verification:** an agent compares the change with the decision",
            "- **Verification:** TODO")
        text = definition(bodies={"Projected foundation changes":
                                  projected(entries="### Decisions\n\n" + decision)})
        self.assertEqual(conditions(text), [])

    def test_todo_on_a_line_continuing_a_field_is_no_gap(self):
        decision = DECISION.replace(
            "- **Verification:** an agent compares the change with the decision",
            "- **Verification:** an agent compares the change with the decision:\n"
            "  - complies: TODO")
        text = definition(bodies={"Projected foundation changes":
                                  projected(entries="### Decisions\n\n" + decision)})
        self.assertEqual(conditions(text), [])

    def test_todo_in_the_fields_and_the_meaning_sentence_of_an_invariant_is_no_gap(self):
        entries = "### Decisions\n\n%s\n\n### Invariants\n\n%s" % (
            DECISION, INVARIANT)
        text = definition(bodies={"Projected foundation changes": projected(entries=entries)})
        self.assertEqual(conditions(text), [])

    def test_todo_in_the_binding_sentence_of_a_projected_entry_is_reported(self):
        # invariant: project-readiness-gate
        decision = DECISION.replace(
            "The archive has no public write API.", "TODO")
        found = conditions(definition(bodies={"Projected foundation changes":
                                              projected(entries="### Decisions\n\n" + decision)}))
        self.assertIn(("a", "`## Projected foundation changes` holds TODO"), found)

    def test_todo_in_the_definition_of_a_projected_term_is_reported(self):
        term = "#### parcel\n\nTODO\n\n- **Not:** none"
        found = conditions(definition(bodies={"Projected foundation changes":
                                              projected(entries="### Glossary\n\n" + term)}))
        self.assertIn(("a", "`## Projected foundation changes` holds TODO"), found)

    def test_todo_in_the_rationale_of_a_projected_decision_is_reported(self):
        decision = DECISION.replace(
            "*Rationale:* publishing is outside the archive's purpose.", "*Rationale:* TODO")
        found = conditions(definition(bodies={"Projected foundation changes":
                                              projected(entries="### Decisions\n\n" + decision)}))
        self.assertIn(("a", "`## Projected foundation changes` holds TODO"), found)

    def test_todo_in_the_rejected_options_of_a_projected_decision_is_reported(self):
        decision = DECISION.replace(
            "*Rejected:* none considered", "*Rejected:* TODO")
        found = conditions(definition(bodies={"Projected foundation changes":
                                              projected(entries="### Decisions\n\n" + decision)}))
        self.assertIn(("a", "`## Projected foundation changes` holds TODO"), found)

    def test_a_field_line_outside_projected_changes_still_holds_todo(self):
        found = conditions(definition(bodies={"Risks": "- **Risk:** TODO"}))
        self.assertIn(("a", "`## Risks` holds TODO"), found)

    def test_a_word_holding_todo_is_no_todo(self):
        text = definition(bodies={"In scope": "- lista TODOs gracza\n- mastodon"})
        self.assertEqual([c for c, _ in conditions(text) if c == "a"], [])

    def test_an_empty_section_is_reported(self):
        # invariant: project-readiness-gate
        found = conditions(definition(bodies={"Risks": ""}))
        self.assertIn(("a", "`## Risks` is empty — write `none` or `TODO`"), found)

    def test_before_approval_the_empty_gate_record_is_no_gap(self):
        text = definition(status="Status: ready for gate", gate="")
        self.assertEqual(conditions(text, before_approval=True), [])


class OpenQuestions(unittest.TestCase):
    def test_a_question_without_its_place_is_reported(self):
        # invariant: project-readiness-gate
        text = definition(bodies={"Open questions": "- Jak mierzymy postęp?"})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_a_question_resolved_in_a_task_needs_its_name(self):
        text = definition(bodies={"Open questions": "- Jak mierzymy postęp? — resolved in: task: "})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_a_place_on_a_continuation_line_counts(self):
        text = definition(bodies={"Open questions":
                                  "- Jak mierzymy postęp\n  na drugiej mapie? — resolved in: breakdown"})
        self.assertEqual(conditions(text), [])

    def test_a_nested_detail_under_a_question_with_its_place_is_no_finding(self):
        text = definition(bodies={"Open questions":
                                  "- Jak mierzymy postęp? — resolved in: breakdown\n"
                                  "  - kontekst: mapa 2"})
        self.assertEqual(conditions(text), [])

    def test_a_place_on_a_nested_detail_is_no_place_of_the_question(self):
        text = definition(bodies={"Open questions":
                                  "- Jak mierzymy postęp?\n\t- detal — resolved in: breakdown"})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_prose_under_open_questions_is_reported(self):
        text = definition(bodies={"Open questions": "Kilka pytań zostaje."})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_none_states_that_there_is_no_question(self):
        self.assertEqual(conditions(definition(bodies={"Open questions": "none"})), [])


WORKING_TABLE = ("### Candidates in progress\n\n"
                 "| # | Settlement | Kind | Source | What the next reader would guess | State |\n"
                 "|---|---|---|---|---|---|\n"
                 "| 1 | Postać należy do jednej drużyny | decision | material: koncepcja §5 "
                 "| model danych drużyny | waiting |")
WORKING_TABLE_MESSAGE = ("the working table of candidates still stands — the step that finds "
                         "foundation entries has not ended")


class Candidates(unittest.TestCase):
    def test_a_projected_section_without_the_candidates_line_is_reported(self):
        # invariant: project-readiness-gate
        found = conditions(definition(bodies={"Projected foundation changes": "none"}))
        self.assertEqual(found, [("f", "`## Projected foundation changes` does not begin with "
                                       "`Candidates: <n> shown, <k> accepted — YYYY-MM-DD`")])

    def test_a_candidates_line_off_its_form_is_reported(self):
        body = projected(first="Candidates: 3 shown, 1 accepted")
        self.assertEqual([c for c, _ in conditions(definition(
            bodies={"Projected foundation changes": body}))], ["f"])

    def test_the_candidates_line_stands_first(self):
        body = "### Decisions\n\n%s\n\n%s" % (DECISION,
                                             CANDIDATES_LINE)
        self.assertEqual([c for c, _ in conditions(definition(
            bodies={"Projected foundation changes": body}))], ["f"])

    def test_more_accepted_than_shown_is_reported(self):
        body = projected(first="Candidates: 1 shown, 3 accepted — 2026-10-03")
        self.assertEqual(conditions(definition(bodies={"Projected foundation changes": body})),
                         [("f", "more candidates accepted than shown")])

    def test_none_below_the_candidates_line_passes(self):
        body = projected(entries="none")
        self.assertEqual(conditions(definition(bodies={"Projected foundation changes": body})), [])

    def test_a_working_table_still_standing_is_reported_before_approval(self):
        # invariant: project-readiness-gate
        body = projected(entries=WORKING_TABLE + "\n\n### Decisions\n\n" + DECISION)
        text = definition(status="Status: ready for gate", gate="",
                          bodies={"Projected foundation changes": body})
        self.assertEqual(conditions(text, before_approval=True), [("f", WORKING_TABLE_MESSAGE)])

    def test_a_section_still_reading_todo_is_one_gap_and_no_f(self):
        text = definition(status="Status: definition — open: Projected foundation changes",
                          gate="", bodies={"Projected foundation changes": "TODO"})
        self.assertEqual(conditions(text, before_approval=True),
                         [("a", "`## Projected foundation changes` holds TODO")])


TECHNOLOGY_PROJECTED = ("- Archiwum dokumentów — projected: What does the archive exclude for good?\n"
                        "- Język i miejsce działania aplikacji — held by: ARC-01")
NONE_MESSAGE = ("`## Technology` reads `none` — list the choices the project needs, each with the "
                "entry that settles it")
NO_MARKER_MESSAGE = ("the choice ends with none of `— held by: <decision>`, "
                     "`— projected: <question>`")
OPEN_MESSAGE = "the choice is still open — the step that settles the technology has not ended"
HELD_FORM_MESSAGE = "`held by:` names no decision as `<PREFIX>-<NN>`"
DANGLING_MESSAGE = ("`projected:` names a question no heading under "
                    "`## Projected foundation changes` holds")


class Technology(unittest.TestCase):
    def technology(self, body, **kwargs):
        return conditions(definition(bodies={"Technology": body}, **kwargs))

    def test_a_definition_without_the_technology_section_is_reported(self):
        # invariant: project-technology-record
        order = [n for n in readiness_check.SECTIONS[:-1] if n != "Technology"]
        self.assertIn(("structure", "the section `## Technology` is missing"),
                      conditions(definition(order=order)))

    def test_none_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("none"), [("g", NONE_MESSAGE)])

    def test_a_choice_without_its_entry_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Magazyn danych"), [("g", NO_MARKER_MESSAGE)])

    def test_an_open_choice_is_reported_before_approval(self):
        # invariant: project-technology-record
        text = definition(status="Status: ready for gate", gate="",
                          bodies={"Technology": "- Magazyn danych — open"})
        self.assertEqual(conditions(text, before_approval=True), [("g", OPEN_MESSAGE)])

    def test_held_by_off_the_identifier_form_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Język — held by: decyzja o języku"),
                         [("g", HELD_FORM_MESSAGE)])

    def test_a_projected_question_no_heading_holds_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Magazyn danych — projected: Where is data stored?"),
                         [("g", DANGLING_MESSAGE)])

    def test_projected_naming_an_invariant_heading_is_reported(self):
        # invariant: project-technology-record
        entries = "### Decisions\n\n%s\n\n### Invariants\n\n%s" % (
            DECISION, INVARIANT)
        text = definition(bodies={
            "Technology": "- Dokumenty — projected: one-workspace-per-document",
            "Projected foundation changes": projected(entries=entries)})
        self.assertEqual(conditions(text), [("g", DANGLING_MESSAGE)])

    def test_held_by_with_a_version_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Magazyn danych — held by: ARC-02/1"),
                         [("g", HELD_FORM_MESSAGE)])

    def test_a_choice_still_open_after_a_held_marker_is_reported(self):
        # invariant: project-technology-record
        found = self.technology("- Magazyn danych — held by: ARC-02 — open")
        self.assertEqual([c for c, _ in found], ["g"])

    def test_projected_with_no_decision_heading_in_the_section_is_reported(self):
        # invariant: project-technology-record
        text = definition(bodies={
            "Technology": "- Magazyn danych — projected: Which database?",
            "Projected foundation changes": projected(
                first="Candidates: 0 shown, 0 accepted — 2026-10-03", entries="none")})
        self.assertEqual(conditions(text), [("g", DANGLING_MESSAGE)])

    def test_projected_matching_the_candidates_line_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Hosting — projected: 2026-10-03"),
                         [("g", DANGLING_MESSAGE)])

    def test_projected_naming_part_of_a_heading_question_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("- Archiwum — projected: What does the archive"),
                         [("g", DANGLING_MESSAGE)])

    def test_a_decision_heading_outside_projected_changes_holds_no_question(self):
        # invariant: project-technology-record
        text = definition(bodies={
            "Background": "Gra istnieje tylko jako koncepcja.\n\n"
                          "#### (new) — Where is data stored?",
            "Technology": "- Magazyn danych — projected: Where is data stored?"})
        self.assertEqual(conditions(text), [("g", DANGLING_MESSAGE)])

    def test_an_open_choice_after_a_settled_one_is_reported(self):
        # invariant: project-technology-record
        body = "- Język aplikacji — held by: ARC-01\n- Magazyn danych — open"
        self.assertEqual(self.technology(body), [("g", OPEN_MESSAGE)])

    def test_none_followed_by_choices_is_reported(self):
        # invariant: project-technology-record
        found = self.technology("none\n- Magazyn danych — open")
        self.assertIn(("g", OPEN_MESSAGE), found)
        self.assertIn(("g", "a line under `## Technology` that is no choice item"), found)

    def test_indented_prose_under_technology_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("  Zostajemy przy obecnym stacku."),
                         [("g", "a line under `## Technology` that is no choice item")])

    def test_prose_under_technology_is_reported(self):
        # invariant: project-technology-record
        self.assertEqual(self.technology("Wszystko jest w fundamencie."),
                         [("g", "a line under `## Technology` that is no choice item")])

    def test_choices_held_and_projected_pass(self):
        self.assertEqual(self.technology(TECHNOLOGY_PROJECTED), [])

    def test_choices_all_held_by_the_foundation_pass(self):
        body = ("- Język i miejsce działania aplikacji — held by: ARC-01\n"
                "- Magazyn kont i zapisów — held by: ARC-02")
        self.assertEqual(self.technology(body), [])

    def test_a_choice_whose_name_holds_a_dash_reads_its_last_marker(self):
        self.assertEqual(self.technology("- Serwer — konta i zapisy — held by: ARC-02"), [])

    def test_a_choice_on_two_lines_counts(self):
        self.assertEqual(self.technology("- Magazyn kont\n  i zapisów — held by: ARC-02"), [])

    def test_a_nested_detail_under_a_choice_is_no_finding(self):
        body = "- Magazyn kont — held by: ARC-02\n  - kontekst: konta graczy"
        self.assertEqual(self.technology(body), [])

    def test_projected_naming_a_change_of_a_current_decision_passes(self):
        decision = DECISION.replace(
            "#### (new) — What does the archive exclude for good?",
            "#### WAY-07 — What does the archive exclude for good?")
        text = definition(bodies={
            "Technology": TECHNOLOGY_PROJECTED,
            "Projected foundation changes": projected(entries="### Decisions\n\n" + decision)})
        self.assertEqual(conditions(text), [])

    def test_a_section_still_reading_todo_is_one_gap_and_no_g(self):
        text = definition(status="Status: definition — open: Technology", gate="",
                          bodies={"Technology": "TODO"})
        self.assertEqual(conditions(text, before_approval=True),
                         [("a", "`## Technology` holds TODO")])


class GateRecord(unittest.TestCase):
    def test_a_missing_gate_record_is_reported_after_approval(self):
        found = conditions(definition(gate=""))
        self.assertIn("e", [c for c, _ in found])

    def test_a_gate_line_off_its_form_is_reported(self):
        gate = ("- Approved by: Mariusz\n- Foundation searched at: 595f839\n"
                "- Definition fingerprint: 00000000")
        found = conditions(definition(gate=gate))
        self.assertIn(("e", "the line is not `- Approved by: …` in its form"), found)

    def test_a_definition_changed_after_the_gate_is_reported(self):
        stale = definition()
        changed = stale.replace("- edytor map", "- edytor map\n- tryb wieloosobowy")
        found = [c for c, _ in conditions(changed)]
        self.assertEqual(found, ["e"])

    def test_a_change_of_spaces_only_keeps_the_fingerprint(self):
        text = definition().replace("Gra istnieje tylko jako koncepcja.",
                                    "Gra istnieje  tylko\njako koncepcja.")
        self.assertEqual(conditions(text), [])

    def test_the_status_line_and_the_gate_record_stay_outside_the_fingerprint(self):
        text = definition().replace("Status: approved 2026-10-03", "Status: approved 2026-10-04")
        self.assertEqual(conditions(text), [])


class Command(unittest.TestCase):
    def run_main(self, text, *args, encoding="utf-8"):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "definition.md")
            with open(path, "w", encoding=encoding, newline="") as handle:
                handle.write(text)
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = readiness_check.main([path, *args])
            return code, out.getvalue(), err.getvalue()

    def test_a_ready_definition_exits_zero(self):
        code, out, _ = self.run_main(definition())
        self.assertEqual((code, out), (0, "readiness: nothing found\n"))

    def test_findings_exit_one(self):
        code, out, _ = self.run_main(definition(bodies={"Risks": "TODO"}))
        self.assertEqual(code, 1)
        self.assertTrue(out.endswith("readiness: 1 finding(s)\n"))

    def test_before_approval_says_what_it_left_out(self):
        code, out, _ = self.run_main(definition(status="Status: ready for gate", gate=""),
                                     "--before-approval")
        self.assertEqual((code, out), (0, "readiness: nothing found (gate record left out: "
                                          "--before-approval)\n"))

    def test_fingerprint_prints_the_definition_fingerprint(self):
        text = definition(gate="")
        content = body_text(BODIES, readiness_check.SECTIONS[:-1])
        code, out, _ = self.run_main(text, "--fingerprint")
        self.assertEqual((code, out), (0, wording_fingerprint(content) + "\n"))

    def test_a_file_that_is_not_utf_8_exits_two(self):
        code, _, err = self.run_main(definition(), encoding="cp1250")
        self.assertEqual(code, 2)
        self.assertIn("is not UTF-8 text", err)

    def test_a_missing_file_exits_two(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = readiness_check.main([os.path.join(tempfile.gettempdir(), "no-such-file.md")])
        self.assertEqual(code, 2)

    def test_a_crlf_definition_gives_the_fingerprint_of_its_lf_copy(self):
        text = definition()
        code, out, _ = self.run_main(text.replace("\n", "\r\n"))
        self.assertEqual((code, out), (0, "readiness: nothing found\n"))


if __name__ == "__main__":
    unittest.main()
