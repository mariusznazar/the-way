"""Tests of how the readiness check reports the three marked choices of the Technology section —
the logs, the interface and the development data through which an agent reaches the running
product (WAY-121): which findings a missing mark gives, and where it gives none.

Run from the root of the-way:
    python -B gate/run_tests.py project-level

The definitions are written out here; the checks of the invariant itself stand in
`test_readiness_check.py`.
"""

import os
import sys
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import readiness_check  # noqa: E402

BEFORE_TECHNOLOGY = """# Archiwum

Status: ready for gate

## Goal

Zespół odnajduje każdy dokument w jednym miejscu.

## Background

Dokumenty leżą w trzech miejscach.

## In scope

- wyszukiwanie dokumentów

## Out of scope

none

## Inputs and constraints

none

## Deliverables

- wyszukiwarka

## Success

Zespół znajduje dokument w minutę.
**OBALENIE:** jeśli szukanie trwa dłużej — rama jest fałszywa.

## Risks

none

## Open questions

none

## Touched parts and decisions

none

## Technology

"""

AFTER_TECHNOLOGY = """

## Projected foundation changes

Candidates: 0 shown, 0 accepted — 2026-10-18
none

## Gate record

none
"""

LANGUAGE = "- Język aplikacji — held by: ARC-01/1"
LOGS = "- logs: Logi w konsoli serwera — held by: ARC-02/1"
INTERFACE = "- interface: Przeglądarka prowadzona przez agenta — held by: ARC-03/1"
DATA = "- development data: Przykładowe dokumenty w repozytorium — held by: ARC-04/1"


def findings(technology):
    text = BEFORE_TECHNOLOGY + technology + AFTER_TECHNOLOGY
    return [(f.condition, f.message) for f in readiness_check.check(text, before_approval=True)]


class MissingMarks(unittest.TestCase):
    def test_the_whole_list_has_no_finding(self):
        self.assertEqual(findings("\n".join([LANGUAGE, LOGS, INTERFACE, DATA])), [])

    def test_each_missing_mark_is_a_finding_of_its_own_naming_it(self):
        found = findings("\n".join([LANGUAGE, INTERFACE]))
        self.assertEqual([c for c, _ in found], ["g", "g"])
        self.assertIn("`logs:`", found[0][1])
        self.assertIn("`development data:`", found[1][1])
        self.assertNotIn("`interface:`", found[0][1] + found[1][1])

    def test_a_section_reading_none_gives_its_one_finding(self):
        found = findings("none")
        self.assertEqual(len(found), 1)
        self.assertIn("reads `none`", found[0][1])

    def test_a_section_still_reading_todo_gives_no_mark_finding(self):
        self.assertEqual([c for c, _ in findings("TODO")], ["a"])


# A definition approved before the three choices were required, as the plan-state checks held it
# at commit 77c8a8b: its gate record's fingerprint is that commit's literal, computed there apart
# from the code under test.
APPROVED_BEFORE = """# Report download

Status: approved 2026-10-01

## Goal

Readers can download a saved report.

## Background

Readers cannot download reports today.

## In scope

- Download a saved report.

## Out of scope

none

## Inputs and constraints

none

## Deliverables

- A downloadable saved report.

## Success

A reader downloads a report.
**FALSIFIED IF:** a saved report cannot be downloaded.

## Risks

none

## Open questions

none

## Touched parts and decisions

none

## Technology

- Existing application language — held by: APP-01/1

## Projected foundation changes

Candidates: 0 shown, 0 accepted — 2026-10-01

none

## Gate record

- Approved by: Mariusz, 2026-10-01
- Foundation searched at: 595f839
- Definition fingerprint: a3b6ab99
"""


class ApprovedBefore(unittest.TestCase):
    def conditions(self, text):
        return [(f.condition, f.message) for f in readiness_check.check(text)]

    def test_it_is_stopped_for_the_three_missing_choices_alone(self):
        found = self.conditions(APPROVED_BEFORE)
        self.assertEqual([c for c, _ in found], ["g", "g", "g"])
        for mark, (_, message) in zip(("`logs:`", "`interface:`", "`development data:`"), found):
            self.assertIn(mark, message)

    def test_once_the_choices_are_added_it_goes_through_the_gate_again(self):
        added = APPROVED_BEFORE.replace(
            "- Existing application language — held by: APP-01/1\n",
            "- Existing application language — held by: APP-01/1\n"
            "- logs: Application log on the server — held by: APP-02/1\n"
            "- interface: The download page in a browser — held by: APP-03/1\n"
            "- development data: Saved reports a script creates — held by: APP-04/1\n")
        self.assertEqual([c for c, _ in self.conditions(added)], ["e"])


if __name__ == "__main__":
    unittest.main()
