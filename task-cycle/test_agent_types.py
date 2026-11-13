"""Content checks of the definitions of the two agent types the task cycle dispatches its stages
with (`task-cycle/agent-types/`): what Claude Code reads from their frontmatter decides what an
agent of the type starts with, so each field is checked, and the fields that must be absent too.

Run from the root of the-way: python -B gate/run_tests.py task-cycle
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parent / "agent-types"
MARK = "Dispatched only by the task cycle of the-way."
# The fields each definition holds, whatever else Claude Code would read: a field outside the list
# could add a tool list, drop the instruction files, or set a model the dispatch sets.
FIELDS = {
    "the-way-stage": {"name", "description", "disallowedTools"},
    "the-way-author": {"name", "description", "disallowedTools", "experimental"},
}


def read(name: str) -> tuple[dict[str, str], list[str], str]:
    """The top-level frontmatter fields as written (a field's value is what follows its colon on
    its line), the indented lines under each field, and the body."""
    text = (DIRECTORY / f"{name}.md").read_text(encoding="utf-8")
    lines = text.split("\n")
    assert lines[0] == "---", name
    end = lines.index("---", 1)
    fields: dict[str, str] = {}
    indented: list[str] = []
    for line in lines[1:end]:
        if line.startswith(" "):
            indented.append(line)
            continue
        key, _, value = line.partition(":")
        fields[key] = value.strip()
    return fields, indented, "\n".join(lines[end + 1:])


class AgentTypeDefinitions(unittest.TestCase):
    def test_the_directory_holds_the_two_definitions_and_nothing_else(self) -> None:
        self.assertEqual(sorted(path.name for path in DIRECTORY.iterdir()),
                         ["the-way-author.md", "the-way-stage.md"])

    def test_each_definition_holds_its_fields_and_no_other(self) -> None:
        for name, expected in FIELDS.items():
            with self.subTest(name):
                fields, _, _ = read(name)
                self.assertEqual(set(fields), expected)
                self.assertEqual(fields["name"], name)
                self.assertTrue(fields["description"].endswith(MARK), fields["description"])

    def test_the_agent_has_every_tool_of_the_session_except_the_skill_tool(self) -> None:
        for name in FIELDS:
            with self.subTest(name):
                fields, _, _ = read(name)
                # No `tools` list: the agent inherits every tool of the session, the tools of
                # connected servers included; the skill tool alone is taken away.
                self.assertNotIn("tools", fields)
                self.assertEqual(fields["disallowedTools"], "Skill")

    def test_the_agent_starts_with_the_instruction_files_of_the_session(self) -> None:
        for name in FIELDS:
            with self.subTest(name):
                fields, _, _ = read(name)
                self.assertNotIn("omitClaudeMd", fields)

    def test_only_the_one_authors_type_has_the_hour_long_cache(self) -> None:
        stage_fields, stage_lines, _ = read("the-way-stage")
        author_fields, author_lines, _ = read("the-way-author")
        self.assertNotIn("experimental", stage_fields)
        self.assertEqual(stage_lines, [])
        self.assertEqual(author_fields["experimental"], "")
        # The key stands inside the `experimental` map, not at the top level of the frontmatter.
        self.assertEqual(author_lines, ["  cacheTtl: 1h"])
        for fields in (stage_fields, author_fields):
            self.assertNotIn("cacheTtl", fields)

    def test_each_body_says_in_two_sentences_at_least_what_the_type_is(self) -> None:
        for name in FIELDS:
            with self.subTest(name):
                _, _, body = read(name)
                sentences = re.findall(r"[^.!?]+[.!?](?:\s|$)", body)
                self.assertGreaterEqual(len(sentences), 2, body)
                self.assertTrue(body.strip().startswith("You are "), body)
                self.assertIn("task cycle of the-way", body)

    def test_the_body_of_each_type_sends_the_agent_to_a_file_for_its_method(self) -> None:
        # An agent without the skill tool must be told to read the method file it is given.
        for name in FIELDS:
            with self.subTest(name):
                _, _, body = read(name)
                self.assertIn("the skill tool", body)
                self.assertIn("method file your handoff names", body)

    def test_the_one_authors_body_says_why_its_cache_lives_an_hour(self) -> None:
        _, _, body = read("the-way-author")
        self.assertIn("resumes you after each review", body)
        self.assertIn("lives an hour", body)


if __name__ == "__main__":
    unittest.main()
