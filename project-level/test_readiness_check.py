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

DECISION = """### (new) — What does the game exclude for good?

The game has no multiplayer mode.

- **Change:** new decision
- **Scope:** game
- **Based on:** none
- **Relations:** none
- **Verification:** level 2 — an agent compares the change with the decision
- **Review when:** none
- **Origin:** none
- **Approved by:** {approval}

*Rationale:* one player is the audience.
*Rejected:* none considered

> **Translation (pl):** Gra nie ma trybu wieloosobowego."""

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
    "Projected foundation changes": DECISION.format(approval="Mariusz, 2026-10-03"),
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


class Whole(unittest.TestCase):
    def test_a_whole_approved_definition_has_no_finding(self):
        self.assertEqual(conditions(definition()), [])

    def test_a_definition_waiting_for_approval_passes_before_approval(self):
        text = definition(status="Status: ready for gate", gate="",
                          bodies={"Projected foundation changes":
                                  DECISION.format(approval="on acceptance")})
        self.assertEqual(conditions(text, before_approval=True), [])


class Structure(unittest.TestCase):
    def test_a_missing_status_line_is_reported(self):
        self.assertEqual(conditions(definition(status="")),
                         [("structure", "no `Status:` line above the first section")])

    def test_a_status_off_its_forms_is_reported(self):
        found = conditions(definition(status="Status: almost done"))
        self.assertEqual([c for c, _ in found], ["structure"])

    def test_a_missing_section_is_reported(self):
        order = [n for n in readiness_check.SECTIONS[:-1] if n != "Risks"]
        found = conditions(definition(order=order))
        self.assertIn(("structure", "the section `## Risks` is missing"), found)

    def test_a_section_standing_twice_is_reported(self):
        order = list(readiness_check.SECTIONS[:-1]) + ["Risks"]
        found = conditions(definition(order=order))
        self.assertIn(("structure", "`## Risks` stands a second time"), found)

    def test_a_section_outside_the_template_is_reported(self):
        text = definition().replace("## Risks", "## Stakeholders\n\nMariusz\n\n## Risks")
        self.assertIn(("structure", "`## Stakeholders` is no section of the template"),
                      conditions(text))

    def test_sections_out_of_order_are_reported(self):
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
        text = definition(bodies={"Success": "TODO"})
        findings = readiness_check.check(text)
        todo = [f for f in findings if f.condition == "a"]
        self.assertEqual(len(todo), 1)
        self.assertEqual(text.splitlines()[todo[0].line - 1], "TODO")

    def test_todo_in_a_projected_decision_is_reported(self):
        decision = DECISION.format(approval="Mariusz, 2026-10-03").replace(
            "- **Review when:** none", "- **Review when:** TODO")
        found = conditions(definition(bodies={"Projected foundation changes": decision}))
        self.assertIn(("a", "`## Projected foundation changes` holds TODO"), found)

    def test_a_word_holding_todo_is_no_todo(self):
        text = definition(bodies={"In scope": "- lista TODOs gracza\n- mastodon"})
        self.assertEqual([c for c, _ in conditions(text) if c == "a"], [])

    def test_an_empty_section_is_reported(self):
        found = conditions(definition(bodies={"Risks": ""}))
        self.assertIn(("a", "`## Risks` is empty — write `none` or `TODO`"), found)

    def test_before_approval_the_empty_gate_record_is_no_gap(self):
        text = definition(status="Status: ready for gate", gate="")
        self.assertEqual(conditions(text, before_approval=True), [])


class OpenQuestions(unittest.TestCase):
    def test_a_question_without_its_place_is_reported(self):
        text = definition(bodies={"Open questions": "- Jak mierzymy postęp?"})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_a_question_resolved_in_a_task_needs_its_name(self):
        text = definition(bodies={"Open questions": "- Jak mierzymy postęp? — resolved in: task: "})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_a_place_on_a_continuation_line_counts(self):
        text = definition(bodies={"Open questions":
                                  "- Jak mierzymy postęp\n  na drugiej mapie? — resolved in: breakdown"})
        self.assertEqual(conditions(text), [])

    def test_prose_under_open_questions_is_reported(self):
        text = definition(bodies={"Open questions": "Kilka pytań zostaje."})
        self.assertEqual([c for c, _ in conditions(text)], ["d"])

    def test_none_states_that_there_is_no_question(self):
        self.assertEqual(conditions(definition(bodies={"Open questions": "none"})), [])


class Approvals(unittest.TestCase):
    def test_a_projected_decision_on_acceptance_is_reported_after_approval(self):
        text = definition(bodies={"Projected foundation changes":
                                  DECISION.format(approval="on acceptance")})
        self.assertIn(("b", "a projected decision still reads `Approved by: on acceptance`"),
                      conditions(text))


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
        self.assertEqual((code, out), (0, "readiness: nothing found (approvals and gate record "
                                          "left out: --before-approval)\n"))

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
