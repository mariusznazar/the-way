"""Tests of task-cycle/request_check.py on descriptions and task documents written for the tests.

Each fixture is text written here, in the form `task-cycle/skill/request_template.md` gives a
request's description and `project-level/task/template.md` and `project-level/plan/template.md` give
a task document and a project plan. Line numbers the tests expect are found in the fixture by the
text of the line, never by the script.
"""

from __future__ import annotations

import io
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import request_check  # noqa: E402

TEMPLATE = HERE / "skill" / "request_template.md"

POLISH_TASK = """\
---
title: "the way: koszt cyklu w jednym wierszu"
status: draft
---

# Opis PR-a podaje koszt cyklu w jednym wierszu, a tabela etapów stoi pod linkiem

Status: ready for cycle
Project relation: independent

## Description

### Need

- Mariusz przy PR-ze patrzy tylko na pytania i na koszt, a tabela etapów stoi dziś w `stages.md`,
  którego nikt nie otwiera (rozmowa 2026-11-05).
- Koszt cyklu jest rozsiany po trzech miejscach opisu, więc trudno go porównać między zadaniami.

### To do

1. Skrypt `task-cycle/cycle_stages.py` zapisuje sumę czasu i tokenów w pierwszym wierszu raportu.
2. Opis PR-a podaje tę sumę w sekcji *Cost*, a link do tabeli etapów stoi zaraz obok niej.
3. Gdy sesja nie ma transkryptu, raport mówi o tym wprost, zamiast pomijać ją po cichu.

### Questions to settle

- What does the request show when the transcript of a session is missing from the home of its
  tool? The answer is the one the human gave, and it stands in the source of the row below.

## Decisions in play

- WAY-160: "The task-cycle orchestrator itself runs the product's gate on the tree that goes into
  the request, and the request gives its command and exit code and names each check that failed."
- WAY-148: "Every task-cycle stage passes its full handoff and report through files in the cycle's
  reports directory, while its messages carry routing, the stage's status, commits, a one-line
  check result naming what failed or did not run, and the report's path."
- WAY-162: "Where a blocking finding remains after that review of the fix, no third round runs,
  the orchestrator does not rule on it, and the cycle opens a draft request marked blocked."
"""

ENGLISH_TASK = """\
# The request shows the cost of the cycle in one line, with the table of stages behind a link

Status: ready for cycle
Project relation: independent

## Description

### Need

- The human looks only at the questions and at the cost of a request, while the table of stages
  stands in a file that nobody opens.
- The cost of a cycle is spread over three places of the description, so it is hard to compare
  between tasks.

### To do

1. The script that counts the stages writes the sum of the time and the tokens in the first line
   of its report.
2. The description of the request gives that sum in its section on the cost, with the link to the
   table beside it.
"""

SHORT_TASK = """\
# Krótkie zadanie

### Need

- Jedna rzecz do zrobienia.
"""

POLISH_PLAN = """\
# Plan projektu: konta graczy

Status: handed over 2026-11-01
Definition: (P) Konta graczy.md — fingerprint 1a2b3c4d

## Tasks

| # | Task | Goal | Depends on | In scope | Preparatory | State | Document |
|---|---|---|---|---|---|---|---|
| 1 | test-server | serwer testowy, na którym każda zmiana jest widoczna, zanim trafi do graczy | — | 4 | yes | to refine | — |
| 2 | player-accounts | gracz zakłada konto i loguje się na nie z każdego urządzenia, które ma | 1 | 1, 2 | no | ready for cycle | — |
| 3 | saved-games | zapisana gra wraca po ponownym zalogowaniu dokładnie w tym miejscu, gdzie gracz ją zostawił | 2 | 3 | no | to refine | — |

## Projected entries

| Entry | Realized by | Written by |
|---|---|---|
| (new) — Who can create and use a player account? | 2 | 2 |
| (new) — How long does the server keep a saved game after its account is removed? | 3 | 3 |
| (new) — Which of the player's devices may hold the session of an account at once? | 2 | 2 |
| player-save-isolation | 3 | 3 |

## Open questions

- Czy gracz może mieć dwa konta na jednym adresie poczty? — definition: task: player-accounts — plan: task 2
- Jak długo serwer trzyma zapis gry po usunięciu konta? — definition: breakdown — answer: as long as the law allows (the definition)

## Phases

none

## Change log

- 2026-11-01 — written from the definition at fingerprint 1a2b3c4d
- 2026-11-02 — the state of task 2 moved to ready for cycle after the human accepted its document
- 2026-11-03 — the state of task 2 moved to in cycle when its cycle started on the branch of its name
- 2026-11-04 — the plan was checked again against the definition after it passed its gate again
"""

ENGLISH_PLAN = """\
# Project plan: player accounts

Status: draft
Definition: (P) Player accounts.md — fingerprint 1a2b3c4d

## Tasks

| # | Task | Goal | Depends on | In scope | Preparatory | State | Document |
|---|---|---|---|---|---|---|---|
| 1 | test-server | a test server on which each change can be seen before it reaches the players | — | 4 | yes | to refine | — |
| 2 | player-accounts | a player creates an account and logs in to it from any device they have | 1 | 1, 2 | no | to refine | — |

## Open questions

- Can a player have two accounts at the same mail address? — definition: task: player-accounts — plan: task 2

## Change log

- 2026-11-01 — written from the definition at fingerprint 1a2b3c4d
"""

VALID = """\
**State: ready** — nothing waits for you beyond the one choice below.

## What you will see

When a cycle opens a request, its description starts with what you decide, and the cost of the
cycle stands in one line at the top of it.

### Underneath

A new script checks the form of the description before the request opens.

## For you to decide

1. The cycle kept the old heading of the record, so that the tests that read it need no change.
   Accept? (Technical changes, 2)

## Cost

2 h 10 min, one model, 3.1 M tokens, two review rounds; [the table of stages](https://example.com/stages.md).

## How to merge

Merge with a merge commit, so that the link to the record keeps working.

<details>
<summary>Po polsku</summary>

**Stan: gotowy** — poza jednym wyborem niżej nic na ciebie nie czeka.

## Co zobaczysz

Gdy cykl otwiera PR, jego opis zaczyna się od tego, o czym decydujesz, a koszt cyklu stoi w jednym
wierszu na samej górze.

### Pod spodem

Nowy skrypt sprawdza formę opisu, zanim PR się otworzy.

## Do twojej decyzji

1. Cykl zostawił stary nagłówek zapisu cyklu, żeby testy, które go czytają, nie wymagały zmian.
   Akceptujesz?

## Koszt

Dwie godziny i dziesięć minut, jeden model, trzy miliony tokenów, dwie rundy przeglądu.

## Jak scalić

Scal commitem scalającym, żeby link do zapisu cyklu dalej działał.

</details>

## Technical changes

1. The description has one template now. It stands in `task-cycle/skill/request_template.md`.
2. The record keeps its heading `## Request handoff`.

## Checks

The gate passed: `python -B gate/run_tests.py`, exit 0.

## Foundation entries

none

## Minor findings

none

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task document, frozen on 2026-11-05.
- **Record:** the commit that adds the record.
"""

ENGLISH_BLOCK = """\
**State: ready** — nothing waits for you beyond the one choice below.

## What you will see

When a cycle opens a request, its description starts with what you decide, and the cost of the
cycle stands in one line at the top of it.
"""

POLISH_PROSE = """\
Opis PR-a z cyklu ma stały schemat: na górze stoi to, co człowiek rozstrzyga, a niżej archiwum,
które czyta agent albo człowiek sprawdzający zmianę uważniej. Decyzja WAY-114 mówi dziś: „the
human accepts the meaning of a foundation entry at the merge of the change that holds it”, więc
przy każdym PR-ze lista wpisów rośnie i nikt jej nie czyta. Zadanie zmienia to tak, że w sekcji
decyzji stoją tylko wpisy, których człowiek nie widział przy dokumencie zadania, a pełna lista
zostaje w archiwum po angielsku. Skrypt `task-cycle/request_check.py` sprawdza kolejność
nagłówków, treść albo `none` w każdej sekcji i obecność zwiniętego bloku w języku zadania. Gdy
skrypt zgłasza błąd, który prowadzący cykl uważa za fałszywy, PR otwiera się jako szkic, a w
sekcji decyzji stoi pytanie, czy scalić go mimo tego.
"""

ENGLISH_PROSE = """\
The description of a request a cycle opens has one shape. The top part is written for the human
in plain words: the state of the request, what changes for the people who use the product, what
waits for the human's yes, the cost of the cycle and how to merge it. It is repeated in the
language of the task document in a collapsed block. Below it, the lower part holds the evidence for
agents and for a human who checks the change closely, in a fixed order, and each of its items opens
with a sentence that a human understands without reading the code.
"""


def line_of(text: str, needle: str, occurrence: int = 1) -> int:
    """The number of the line of `text` holding `needle` for the `occurrence`-th time."""
    seen = 0
    for number, line in enumerate(text.splitlines(), 1):
        if needle in line:
            seen += 1
            if seen == occurrence:
                return number
    raise AssertionError(f"{needle!r} not found {occurrence} time(s)")


def with_block(description: str, content: str) -> str:
    """`description` with the content of its block, after `</summary>`, replaced."""
    start = description.index("<summary>Po polsku</summary>\n") + len("<summary>Po polsku</summary>\n")
    end = description.index("</details>\n\n## Technical changes")
    return description[:start] + content + description[end:]


class Checked:
    def __init__(self, description: str, task: str) -> None:
        self.result = request_check.check(description, task)
        self.lines = [number for number, _ in self.result.problems]
        self.text = "\n".join(f"line {number}: {message}"
                              for number, message in self.result.problems)


class ValidTest(unittest.TestCase):
    def test_a_whole_description_with_a_polish_block_for_a_polish_task_passes(self) -> None:
        checked = Checked(VALID, POLISH_TASK)
        self.assertEqual(checked.result.problems, [])
        self.assertEqual(checked.result.task_language, "not English")
        self.assertEqual(checked.result.block_language, "not English")

    def test_an_english_task_with_a_none_block_passes(self) -> None:
        checked = Checked(with_block(VALID, "\nnone\n\n"), ENGLISH_TASK)
        self.assertEqual(checked.result.problems, [])
        self.assertEqual(checked.result.task_language, "English")

    def test_the_tasks_own_sections_in_their_slot_pass(self) -> None:
        description = VALID.replace(
            "## Course of the cycle",
            "## Proposals for the skills\n\n1. A proposal not applied.\n\n"
            "## Audit of the series\n\nnone\n\n## Course of the cycle")
        self.assertEqual(Checked(description, POLISH_TASK).result.problems, [])

    def test_the_sections_found_are_named(self) -> None:
        sections = Checked(VALID, POLISH_TASK).result.sections
        self.assertEqual(sections[0], "What you will see")
        self.assertEqual(sections[-1], "Course of the cycle")
        self.assertIn("Findings outside the task's scope", sections)


class StateLineTest(unittest.TestCase):
    def test_a_first_line_without_the_bold_state_is_reported(self) -> None:
        description = VALID.replace("**State: ready** — nothing", "State: ready — nothing", 1)
        self.assertEqual(Checked(description, POLISH_TASK).lines, [1])

    def test_a_state_outside_the_three_words_is_reported(self) -> None:
        description = VALID.replace("**State: ready**", "**State: done**", 1)
        self.assertEqual(Checked(description, POLISH_TASK).lines, [1])

    def test_a_state_with_no_reason_after_the_dash_is_reported(self) -> None:
        description = VALID.replace(
            "**State: ready** — nothing waits for you beyond the one choice below.",
            "**State: ready** —", 1)
        self.assertEqual(Checked(description, POLISH_TASK).lines, [1])

    def test_the_state_line_is_the_first_line_that_is_not_blank(self) -> None:
        self.assertEqual(Checked("\n\n" + VALID, POLISH_TASK).result.problems, [])
        description = "## What you will see\n\n" + VALID
        self.assertIn(1, Checked(description, POLISH_TASK).lines)

    def test_each_of_the_three_states_passes(self) -> None:
        for state in ("ready", "draft", "blocked"):
            description = VALID.replace("**State: ready**", f"**State: {state}**", 1)
            self.assertEqual(Checked(description, POLISH_TASK).result.problems, [], state)


class HeadingTest(unittest.TestCase):
    def test_a_missing_heading_is_reported_where_it_should_stand(self) -> None:
        description = VALID.replace(
            "## Cost\n\n2 h 10 min, one model, 3.1 M tokens, two review rounds; "
            "[the table of stages](https://example.com/stages.md).\n\n", "")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## How to merge")])
        self.assertIn("## Cost", checked.text)

    def test_a_missing_last_heading_is_reported_at_the_end(self) -> None:
        description = VALID[:VALID.index("## Course of the cycle")]
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [len(description.splitlines()) + 1])
        self.assertIn("## Course of the cycle", checked.text)

    def test_a_repeated_heading_is_reported_at_its_second_place(self) -> None:
        description = VALID.replace("## Foundation entries\n",
                                    "## Checks\n\nAgain.\n\n## Foundation entries\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## Checks", 2)])
        self.assertIn("repeated", checked.text)

    def test_a_heading_out_of_order_is_reported(self) -> None:
        cost = ("## Cost\n\n2 h 10 min, one model, 3.1 M tokens, two review rounds; "
                "[the table of stages](https://example.com/stages.md).\n\n")
        description = VALID.replace(cost, "").replace("## For you to decide", cost
                                                       + "## For you to decide")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## For you to decide")])
        self.assertIn("order", checked.text)

    def test_a_missing_underneath_is_reported(self) -> None:
        description = VALID.replace(
            "### Underneath\n\nA new script checks the form of the description before the "
            "request opens.\n\n", "")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## What you will see")])
        self.assertIn("### Underneath", checked.text)

    def test_underneath_in_another_section_is_missing_from_what_you_will_see(self) -> None:
        underneath = ("### Underneath\n\nA new script checks the form of the description before "
                      "the request opens.\n\n")
        description = VALID.replace(underneath, "").replace("## Cost\n\n", "## Cost\n\n"
                                                             + underneath)
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## What you will see")])

    def test_a_heading_not_in_the_template_outside_the_slot_is_reported(self) -> None:
        description = VALID.replace("## Foundation entries\n",
                                    "## Notes\n\nA note.\n\n## Foundation entries\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## Notes")])

    def test_a_heading_not_in_the_template_in_the_top_part_is_reported(self) -> None:
        description = VALID.replace("## Cost\n", "## Summary\n\nA summary.\n\n## Cost\n")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## Summary")])

    def test_a_heading_after_the_course_of_the_cycle_is_reported(self) -> None:
        description = VALID + "\n## Proposals for the skills\n\nA proposal.\n"
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## Proposals for the skills")])

    def test_headings_inside_fenced_code_are_not_headings(self) -> None:
        description = VALID.replace(
            "## Checks\n\n",
            "## Checks\n\n```markdown\n## Cost\n\n## Notes\n```\n\n~~~\n## Checks\n~~~\n\n")
        self.assertEqual(Checked(description, POLISH_TASK).result.problems, [])

    def test_headings_inside_the_block_are_not_headings(self) -> None:
        description = with_block(VALID, "\n## Checks\n\n## Notatki\n\nTo jest notatka, którą "
                                        "agent zostawił dla człowieka, żeby ją przeczytał.\n\n"
                                        "Gdy cykl otwiera PR, jego opis zaczyna się od tego, o "
                                        "czym decydujesz, a koszt stoi w jednym wierszu.\n\n")
        self.assertEqual(Checked(description, POLISH_TASK).result.problems, [])

    def test_a_heading_with_control_characters_is_reported_printable(self) -> None:
        description = VALID.replace("## Foundation entries\n",
                                    "## Notes\x1b[31m\n\nA note.\n\n## Foundation entries\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(len(checked.lines), 1)
        self.assertNotIn("\x1b", checked.text)
        self.assertIn("\\x1b", checked.text)


class ContentTest(unittest.TestCase):
    def test_a_section_with_no_content_is_reported(self) -> None:
        description = VALID.replace("## Minor findings\n\nnone\n\n", "## Minor findings\n\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## Minor findings")])

    def test_a_section_holding_only_a_comment_has_no_content(self) -> None:
        description = VALID.replace("## Minor findings\n\nnone\n\n",
                                    "## Minor findings\n\n<!-- the Minor findings,\n"
                                    "each with the reviewer's words -->\n\n")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## Minor findings")])

    def test_the_last_section_with_no_content_is_reported(self) -> None:
        description = VALID[:VALID.index("- **Task and sources:**")]
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## Course of the cycle")])

    def test_what_you_will_see_with_nothing_before_underneath_is_reported(self) -> None:
        description = VALID.replace(
            "When a cycle opens a request, its description starts with what you decide, and the "
            "cost of the\ncycle stands in one line at the top of it.\n\n", "")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## What you will see")])

    def test_an_empty_underneath_is_reported(self) -> None:
        description = VALID.replace(
            "A new script checks the form of the description before the request opens.\n\n", "")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "### Underneath")])

    def test_how_to_merge_holding_only_the_block_is_reported(self) -> None:
        description = VALID.replace(
            "Merge with a merge commit, so that the link to the record keeps working.\n\n", "")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## How to merge")])

    def test_an_empty_block_is_reported(self) -> None:
        description = with_block(VALID, "\n<!-- the top part in the task's language -->\n\n")
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "<details>")])


class BlockTest(unittest.TestCase):
    def test_no_block_is_reported(self) -> None:
        start = VALID.index("<details>")
        end = VALID.index("</details>\n") + len("</details>\n")
        description = VALID[:start] + VALID[end:]
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "## Technical changes")])
        self.assertIn("<details>", checked.text)

    def test_a_block_after_the_lower_part_is_not_in_its_place(self) -> None:
        start = VALID.index("<details>")
        end = VALID.index("</details>\n") + len("</details>\n")
        description = VALID[:start] + VALID[end:] + "\n" + VALID[start:end]
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "## Technical changes")])

    def test_two_blocks_are_reported(self) -> None:
        start = VALID.index("<details>")
        end = VALID.index("</details>\n") + len("</details>\n")
        description = VALID[:end] + "\n" + VALID[start:end] + VALID[end:]
        self.assertEqual(Checked(description, POLISH_TASK).lines,
                         [line_of(description, "<details>", 2)])

    def test_a_block_not_closed_is_reported(self) -> None:
        description = VALID.replace("</details>\n", "", 1)
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "<details>")])
        self.assertIn("</details>", checked.text)

    def test_a_second_details_in_the_lower_part_is_not_the_block(self) -> None:
        description = VALID.replace(
            "## Checks\n\n",
            "## Checks\n\n<details>\n<summary>The output of the gate</summary>\n\n"
            "Ran 617 tests in 8 directories, and every one of them passed with no warning at "
            "all.\n\n## Cost\n\n</details>\n\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.result.problems, [])
        self.assertEqual(checked.result.block_language, "not English")

    def test_a_block_on_one_line_is_read(self) -> None:
        start = VALID.index("<details>")
        end = VALID.index("</details>\n") + len("</details>\n")
        description = (VALID[:start] + "<details><summary>In the task's language</summary>none"
                       "</details>\n" + VALID[end:])
        self.assertEqual(Checked(description, ENGLISH_TASK).result.problems, [])

    def test_a_nested_details_stays_inside_the_block(self) -> None:
        description = with_block(VALID, "\n<details>\n<summary>Więcej</summary>\n\nSzczegóły, "
                                        "które człowiek może rozwinąć, gdy zechce.\n\n</details>"
                                        "\n\nGdy cykl otwiera PR, jego opis zaczyna się od tego, "
                                        "o czym decydujesz, a koszt cyklu stoi w jednym wierszu "
                                        "na samej górze.\n\n")
        self.assertEqual(Checked(description, POLISH_TASK).result.problems, [])


class LanguageTest(unittest.TestCase):
    def test_an_english_task_with_a_translated_block_is_reported(self) -> None:
        checked = Checked(VALID, ENGLISH_TASK)
        self.assertEqual(checked.lines, [line_of(VALID, "<details>")])
        self.assertIn("none", checked.text)

    def test_a_polish_task_with_a_none_block_is_reported(self) -> None:
        description = with_block(VALID, "\nnone\n\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "<details>")])

    def test_a_polish_task_with_an_untranslated_block_is_reported(self) -> None:
        description = with_block(VALID, "\n" + ENGLISH_BLOCK + "\n")
        checked = Checked(description, POLISH_TASK)
        self.assertEqual(checked.lines, [line_of(description, "<details>")])
        self.assertEqual(checked.result.block_language, "English")

    def test_the_task_is_measured_on_its_title_need_and_to_do_alone(self) -> None:
        # Its whole text is English by the measure; its English questions and decisions do not
        # make it English.
        self.assertGreaterEqual(request_check.english_share(POLISH_TASK)[0],
                                request_check.ENGLISH_THRESHOLD)
        self.assertEqual(Checked(VALID, POLISH_TASK).result.task_language, "not English")
        english_need = POLISH_TASK.replace(
            POLISH_TASK[POLISH_TASK.index("### Need"):POLISH_TASK.index("### Questions")],
            ENGLISH_TASK[ENGLISH_TASK.index("### Need"):] + "\n")
        self.assertEqual(Checked(VALID, english_need).result.task_language, "English")

    def test_a_short_task_is_not_judged_and_passes(self) -> None:
        for content in ("\nnone\n\n", "\n" + ENGLISH_BLOCK + "\n"):
            checked = Checked(with_block(VALID, content), SHORT_TASK)
            self.assertEqual(checked.result.problems, [])
            self.assertEqual(checked.result.task_language, "not judged")

    def test_a_short_block_for_a_polish_task_is_not_judged(self) -> None:
        checked = Checked(with_block(VALID, "\nZobacz wyżej, w części po angielsku.\n\n"),
                          POLISH_TASK)
        self.assertEqual(checked.result.problems, [])
        self.assertEqual(checked.result.block_language, "not judged")

    def test_a_polish_plan_with_english_markers_is_not_english(self) -> None:
        # Its whole text is English by the measure: the markers, states and entries are English.
        self.assertGreaterEqual(request_check.english_share(POLISH_PLAN)[0],
                                request_check.ENGLISH_THRESHOLD)
        self.assertEqual(Checked(VALID, POLISH_PLAN).result.task_language, "not English")
        self.assertEqual(Checked(VALID, POLISH_PLAN).result.problems, [])

    def test_an_english_plan_is_english(self) -> None:
        checked = Checked(with_block(VALID, "\nnone\n\n"), ENGLISH_PLAN)
        self.assertEqual(checked.result.task_language, "English")
        self.assertEqual(checked.result.problems, [])

    def test_prose_falls_on_its_side_of_the_threshold_with_a_margin(self) -> None:
        english_share, english_words = request_check.english_share(ENGLISH_PROSE)
        polish_share, polish_words = request_check.english_share(POLISH_PROSE)
        self.assertGreaterEqual(min(english_words, polish_words), request_check.MINIMUM_WORDS)
        self.assertGreaterEqual(english_share, request_check.ENGLISH_THRESHOLD * 1.5)
        self.assertLessEqual(polish_share, request_check.ENGLISH_THRESHOLD / 2)

    def test_code_urls_and_tags_are_not_counted(self) -> None:
        share, words = request_check.english_share(
            "Zdanie po polsku `the code of the script` [link](https://example.com/the/of/and) "
            "<span title=\"the\">tekst</span>\n```\nthe and of\n```\n")
        self.assertEqual(share, 0)
        self.assertEqual(words, 5)


def run_main(arguments: list[str]) -> tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = request_check.main(arguments)
    return code, stdout.getvalue(), stderr.getvalue()


class CommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.task = self.root / "task.md"
        self.task.write_text(POLISH_TASK, encoding="utf-8")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def write(self, text: str) -> str:
        path = self.root / "request.md"
        path.write_text(text, encoding="utf-8")
        return str(path)

    def test_a_form_that_holds_exits_zero_with_a_summary(self) -> None:
        code, out, _ = run_main([self.write(VALID), "--task", str(self.task)])
        self.assertEqual(code, 0)
        self.assertEqual(len(out.splitlines()), 1)
        self.assertIn("task: not English", out)

    def test_problems_exit_one_each_on_its_line_in_file_order(self) -> None:
        description = VALID.replace("**State: ready**", "State:", 1).replace(
            "## Minor findings\n\nnone\n\n", "## Minor findings\n\n")
        code, out, _ = run_main([self.write(description), "--task", str(self.task)])
        self.assertEqual(code, 1)
        lines = out.splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(lines[0].startswith("line 1: "))
        self.assertTrue(lines[1].startswith(f"line {line_of(description, '## Minor findings')}: "))

    def test_a_wrong_argument_exits_two(self) -> None:
        for arguments in ([self.write(VALID)], [], [self.write(VALID), "--task"]):
            code, out, err = run_main(arguments)
            self.assertEqual(code, 2, arguments)
            self.assertEqual(out, "")
            self.assertTrue(err.startswith("Error: "), err)

    def test_an_unreadable_file_exits_two(self) -> None:
        (self.root / "latin.md").write_bytes("zażółć".encode("cp1250"))
        for arguments in ([str(self.root / "missing.md"), "--task", str(self.task)],
                          [str(self.root / "latin.md"), "--task", str(self.task)],
                          [self.write(VALID), "--task", str(self.root / "latin.md")]):
            code, out, err = run_main(arguments)
            self.assertEqual(code, 2, arguments)
            self.assertEqual(out, "")
            self.assertTrue(err.startswith("Error: "), err)


class TemplateTest(unittest.TestCase):
    def test_the_templates_skeleton_has_the_scripts_headings(self) -> None:
        text = TEMPLATE.read_text(encoding="utf-8")
        skeleton = re.search(r"^```markdown\n(.*?)^```$", text, re.S | re.M)
        self.assertIsNotNone(skeleton, "no fenced markdown block in the template")
        headings = [(len(match.group(1)), match.group(2)) for match in
                    re.finditer(r"^(#{2,3}) (.+)$", skeleton.group(1), re.M)]
        expected = [(2, heading) for heading in request_check.TOP_HEADINGS]
        expected.insert(1, (3, request_check.UNDERNEATH))
        expected += [(2, heading) for heading in request_check.LOWER_HEADINGS[:-1]]
        expected += [(2, request_check.OWN_SECTIONS_PLACEHOLDER),
                     (2, request_check.LOWER_HEADINGS[-1])]
        self.assertEqual(headings, expected)

if __name__ == "__main__":
    unittest.main()
