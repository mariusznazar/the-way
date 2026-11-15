"""Tests of task-cycle/cycle_measures.py on small transcripts and rollouts in the form Claude Code and
Codex keep them in.

The expected figures are worked out by hand from the transcripts written here, not by the script.
"""

from __future__ import annotations

import ast
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "cycle_measures.py"

sys.path.insert(0, str(HERE))

import cycle_measures  # noqa: E402

DAY = "2026-10-06T"
SESSION = "cycle1"


def at(clock: str) -> str:
    return f"{DAY}{clock}.000Z"


def write_lines(path: Path, entries: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(entry) + "\n" for entry in entries), encoding="utf-8")
    return path


def response(clock: str, ident: str, input_tokens: int = 0, read: int = 0, write: int = 0,
             output: int = 1, five: int | None = None, model: str = "opus") -> dict:
    """A Claude Code response line. The whole write is in the 5-minute cache unless `five` says
    otherwise; the rest of it is in the 1-hour cache."""
    five = write if five is None else five
    return {"type": "assistant", "timestamp": at(clock), "message": {
        "id": ident, "model": model, "content": [{"type": "text"}],
        "usage": {"input_tokens": input_tokens, "cache_read_input_tokens": read,
                  "cache_creation_input_tokens": write, "output_tokens": output,
                  "cache_creation": {"ephemeral_5m_input_tokens": five,
                                     "ephemeral_1h_input_tokens": write - five}}}}


def prompt(clock: str, text: str) -> dict:
    return {"type": "user", "timestamp": at(clock),
            "message": {"role": "user", "content": text}}


def tool_call(clock: str, ident: str, tool_id: str, name: str, tool_input: object) -> dict:
    """A Claude Code response line whose one content block is a tool call."""
    line = response(clock, ident)
    line["message"]["content"] = [{"type": "tool_use", "id": tool_id, "name": name,
                                   "input": tool_input}]
    return line


def tool_return(clock: str, tool_id: str, content: object) -> dict:
    """The line that holds the result of a tool call."""
    return {"type": "user", "timestamp": at(clock), "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": tool_id, "content": content}]}}


def minutes(first: int, count: int) -> list[str]:
    """Clock times one minute apart, from the given minute of the morning."""
    return [f"09:{first + index:02d}:00" for index in range(count)]


class MeasuresTest(unittest.TestCase):
    """Each test writes a cycle record of its own in a folder that is removed afterwards."""

    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.root = Path(self.folder.name)
        self.home = self.root / "claude"
        self.project = self.home / "projects" / "C--repo"
        self.env = mock.patch.dict(os.environ, {}, clear=False)
        self.env.start()
        for name in ("CLAUDE_CODE_SESSION_ID", "CODEX_SESSION_ID"):
            os.environ.pop(name, None)

    def tearDown(self) -> None:
        self.env.stop()
        self.folder.cleanup()

    def run_script(self, *args: str) -> tuple[int, str]:
        """Runs the command in-process and returns its exit code and what it wrote to stderr."""
        errors = io.StringIO()
        with redirect_stderr(errors):
            code = cycle_measures.main([*args, "--claude-home", str(self.home),
                                        "--codex-home", str(self.root / "codex")])
        return code, errors.getvalue()

    def session(self, entries: list[dict], name: str = SESSION) -> Path:
        return write_lines(self.project / f"{name}.jsonl", entries)

    def measures(self, *args: str) -> str:
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(*args, "--output", str(output))
        self.assertEqual(0, code, errors)
        return output.read_bytes().decode("utf-8")

    def lines_of(self, text: str) -> list[str]:
        return text.split("\n")


class HandWorkedCycleTest(MeasuresTest):
    """One orchestrator and three subagents, with every figure of the file worked out by hand.

    Orchestrator, in time order (context = input + read + write):
      o1 09:00 input 100, read 0, write 1000 (5-minute), context 1100. Written over two lines
         that repeat it; the first line's input (999) is not the one counted, the second has the
         most output tokens.
      o2 09:10 input 5, read 1100, write 3000 (1-hour), context 4105. A synthetic line at 09:10:30
         with no usage at all is no call.
      o3 09:20 input 3, read 200, write 4000 (5-minute), context 4203.
      Rewrite between o2 and o3: held 1100 + 3000 = 4100, read 200, so 3900; above 2000 and the
      context grew: counted once.
    Subagent a1, meta "implement task 1 (general-purpose)":
      s1 input 10, read 0, write 500 (5-minute), context 510.
      s2 input 1, read 400, write 2500 (1-hour), context 2901. Rewrite against s1: 500 - 400 = 100,
      not above 2000.
      s3 input 2, read 500, write 4000 (5-minute), context 4502. Rewrite against s2: 2900 - 500 =
      2400, above 2000 and the context grew: counted.
    Subagent a2, no meta file: n1 input 1, write 300 (5-minute), context 301.
    Subagent a3, a subagent of a1 by its meta: nested check (Explore): one call, context 10.
    """

    def setUp(self) -> None:
        super().setUp()
        self.session([
            prompt("09:00:00", "run the cycle"),
            response("09:00:00", "o1", input_tokens=999, write=1000, output=10),
            response("09:00:01", "o1", input_tokens=100, write=1000, output=50, five=1000),
            response("09:10:00", "o2", input_tokens=5, read=1100, write=3000, output=20, five=0),
            {"type": "assistant", "timestamp": at("09:10:30"), "message": {
                "id": "synthetic", "model": "<synthetic>", "usage": {}}},
            response("09:20:00", "o3", input_tokens=3, read=200, write=4000, output=30),
        ])
        agents = self.project / SESSION / "subagents"
        write_lines(agents / "agent-a1.jsonl", [
            prompt("09:01:00", "implement task 1"),
            response("09:01:00", "s1", input_tokens=10, write=500, output=5),
            response("09:02:00", "s2", input_tokens=1, read=400, write=2500, output=6, five=0),
            response("09:03:00", "s3", input_tokens=2, read=500, write=4000, output=7),
        ])
        (agents / "agent-a1.meta.json").write_text(json.dumps(
            {"description": "implement task 1", "agentType": "general-purpose"}),
            encoding="utf-8")
        write_lines(agents / "agent-a2.jsonl", [
            response("09:04:00", "n1", input_tokens=1, write=300, output=1),
        ])
        write_lines(agents / "agent-a3.jsonl", [
            response("09:05:00", "x1", input_tokens=4, read=6, output=2),
        ])
        (agents / "agent-a3.meta.json").write_text(json.dumps(
            {"description": "nested check", "agentType": "Explore", "parentAgentId": "a1"}),
            encoding="utf-8")

    def test_every_line_of_the_file_matches_the_hand_worked_figures(self) -> None:
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertEqual([
            "# Measures of the cycle run",
            "",
            "- Calls in all: 8",
            "- Calls of the orchestrator: 3",
            "- Calls of subagents: 5",
            "- Mean context per call: 2204",
            "- Mean context per call of the orchestrator: 3136",
            "- Share of the context in calls above 200000 tokens: 0.0%",
            "- Context of the orchestrator's first call: 1100",
            "- Context of the orchestrator's middle call: 4105",
            "- Context of the orchestrator's last call: 4203",
            "- Cache written, 5 minutes: 9800",
            "- Cache written, 1 hour: 5500",
            "- Cache written again by the orchestrator: 3900",
            "- Calls of the orchestrator with a cache write again: 1",
            "- Cache written again by subagents: 2400",
            "- Calls of subagents with a cache write again: 1",
            "",
            "## Agents",
            "",
            "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
            "| Cache written, 1 hour | Cache written again | Calls with a cache write again "
            + NEW_COLUMNS,
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            f"| orchestrator {SESSION} | Claude Code | 3 | 1100 | 4105 | 4203 | 5000 | 3000 | 3900 | 1 "
            "| 0 | 0 | 0 | 0 |",
            "| implement task 1 (general-purpose) | Claude Code | 3 | 510 | 2901 | 4502 | 4500 "
            "| 2500 | 2400 | 1 | 0 | 0 | 0 | 0 |",
            "| a2 | Claude Code | 1 | 301 | 301 | 301 | 300 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |",
            "| nested check (Explore) | Claude Code | 1 | 10 | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 "
            "| 0 |",
            "",
        ], self.lines_of(text))

    def test_a_response_over_several_lines_counts_once_with_the_line_of_most_output(self) -> None:
        # The first line of o1 has input 999; only the line with the most output (input 100) counts,
        # so the orchestrator's first call has context 1100, not 1999.
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Context of the orchestrator's first call: 1100\n", text)

    def test_a_synthetic_response_is_no_call(self) -> None:
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Calls of the orchestrator: 3\n", text)

    def test_a_nested_subagent_is_an_agent_of_its_own(self) -> None:
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("| nested check (Explore) | Claude Code | 1 | 10 | 10 | 10 |", text)
        self.assertIn("- Calls of subagents: 5\n", text)

    def test_the_same_input_gives_the_same_bytes_on_a_second_run(self) -> None:
        first = self.measures(str(self.project / f"{SESSION}.jsonl"))
        second = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertEqual(first.encode("utf-8"), second.encode("utf-8"))
        self.assertNotIn("\r", first)

    def test_a_session_given_by_its_id_is_found_in_the_claude_home(self) -> None:
        by_path = self.measures(str(self.project / f"{SESSION}.jsonl"))
        by_id = self.measures(SESSION)
        self.assertEqual(by_path, by_id)


LOG = "foundations/decisions.md"
TITLE_INDEX = "# decision_index.py: index of the decisions of the log"  # 54 bytes
TITLE_SECTIONS = "# decision_index.py: list of the sections of the log"  # 52 bytes
NEW_COLUMNS = ("| Decision log bytes | Decision log reads | Decision index bytes "
               "| Decision index reads |")


class ReadsTestCase(MeasuresTest):
    """The figures of the decision log and the index, read from the transcript of an agent."""

    def row_of(self, text: str, start: str) -> list[str]:
        """The cells of the table row that begins with `start`."""
        row = next(line for line in self.lines_of(text) if line.startswith(start))
        return [cell.strip() for cell in row.strip("|").split("|")]

    def figures(self, entries: list[dict]) -> list[str]:
        """The last four cells of the orchestrator's row: log bytes, log reads, index bytes, index
        reads."""
        self.session(entries)
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        return self.row_of(text, f"| orchestrator {SESSION} |")[-4:]


class DecisionLogReadsTest(ReadsTestCase):
    """The bytes of the decision log and of the index that entered an agent's context, and how many
    times, each figure worked out by hand from the transcript written here.

    Only relative paths are written in the transcripts."""

    def test_a_read_of_the_log_counts_its_bytes_and_one_read(self) -> None:
        # The result "héllo log" is h, é (2 bytes), l, l, o, a space and l, o, g: 10 bytes.
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "héllo log"),
        ]))

    def test_the_table_of_agents_ends_with_the_four_columns_after_the_old_ones(self) -> None:
        self.session([tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
                      tool_return("09:01:05", "t1", "héllo log")])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn(
            "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
            "| Cache written, 1 hour | Cache written again | Calls with a cache write again "
            + NEW_COLUMNS + "\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- "
            "| --- | --- |\n", text)

    def test_a_cycle_of_reads_has_hand_worked_figures_for_each_agent(self) -> None:
        """The orchestrator reads the log with a Read (10 bytes) and by a shell command with a
        backslash path (a result of two text blocks, "ab" and "cé", and an image block: 5 bytes),
        reads an index file (70 bytes), and makes calls that are no reads of the log or of the index.
        Its subagent reads the log by a path that begins with ./ (3 bytes) and the list of sections
        by a shell command (53 bytes: 52 and a newline)."""
        self.session([
            prompt("09:00:00", "run"),
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "héllo log"),
            tool_call("09:02:00", "c2", "t2", "Bash", {
                "command": "grep -n WAY-339 .the-way\\foundations\\decisions.md | head -3"}),
            tool_return("09:02:05", "t2", [{"type": "text", "text": "ab"},
                                           {"type": "image", "source": {}},
                                           {"type": "text", "text": "cé"}]),
            tool_call("09:03:00", "c3", "t3", "Read", {"file_path": "task-cycle/index.md"}),
            tool_return("09:03:05", "t3", "     1" + chr(9) + TITLE_INDEX + "\n     2" + chr(9) + "\n"),
            tool_call("09:04:00", "c4", "t4", "Grep", {"pattern": "decisions.md", "path": "foundations"}),
            tool_return("09:04:05", "t4", "no match"),
            tool_call("09:05:00", "c5", "t5", "Read", {"file_path": LOG + ".bak"}),
            tool_return("09:05:05", "t5", "zzz"),
            tool_call("09:06:00", "c6", "t6", "Read", {"file_path": "my" + LOG}),
            tool_return("09:06:05", "t6", "zzz"),
            tool_call("09:07:00", "c7", "t7", "Read", {"file_path": "elements/common/decision_index.py"}),
            tool_return("09:07:05", "t7", 'TITLE = "' + TITLE_INDEX + '"\n'),
            tool_return("09:08:05", "ghost", "the log, though no call of this agent names its id"),
        ])
        agents = self.project / SESSION / "subagents"
        write_lines(agents / "agent-a1.jsonl", [
            tool_call("09:09:00", "d1", "u1", "Read", {"file_path": "./" + LOG}),
            tool_return("09:09:05", "u1", "xyz"),
            tool_call("09:10:00", "d2", "u2", "Bash", {"command": "cat sections.md"}),
            tool_return("09:10:05", "u2", TITLE_SECTIONS + "\n"),
        ])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertEqual(["15", "2", "70", "1"], self.row_of(text, f"| orchestrator {SESSION} |")[-4:])
        self.assertEqual(["3", "1", "53", "1"], self.row_of(text, "| a1 |")[-4:])

    def test_a_result_with_no_call_before_it_a_call_with_no_result_and_a_second_result_are_not_counted(
            self) -> None:
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_return("09:00:30", "t0", "before its call"),
            tool_call("09:01:00", "c0", "t0", "Read", {"file_path": LOG}),
            tool_call("09:02:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:02:05", "t1", "héllo log"),
            tool_return("09:02:06", "t1", "a second result of the same call"),
            tool_call("09:03:00", "c2", "t2", "Read", {"file_path": LOG}),
        ]))

    def test_a_repeated_call_id_counts_once(self) -> None:
        # The same call written on two lines, and a result: one read, not two. The call that comes
        # again after its result is no new read.
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_call("09:01:01", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "héllo log"),
            tool_call("09:01:06", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:07", "t1", "héllo log"),
        ]))

    def test_a_call_id_written_twice_is_a_read_of_the_log_where_either_line_names_it(self) -> None:
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_call("09:01:01", "c1", "t1", "Read", {"file_path": "elsewhere.md"}),
            tool_return("09:01:05", "t1", "héllo log"),
        ]))
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": "elsewhere.md"}),
            tool_call("09:01:01", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "héllo log"),
        ]))

    def test_lines_of_another_type_than_assistant_and_user_are_not_read(self) -> None:
        use = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
        back = tool_return("09:01:05", "t1", "héllo log")
        use["type"] = "api-request-blob"
        back["type"] = "api-request-blob"
        self.assertEqual(["0", "0", "0", "0"], self.figures([use, back]))

    def test_a_result_in_an_assistant_line_is_not_read(self) -> None:
        use = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
        back = tool_return("09:01:05", "t1", "héllo log")
        back["type"] = "assistant"
        back["message"].update({key: value for key, value in response("09:01:05", "r1")["message"].items()
                                if key != "content"})
        self.assertEqual(["0", "0", "0", "0"], self.figures([use, back]))

    def test_a_tool_call_in_a_user_line_is_no_call(self) -> None:
        use = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
        use["type"] = "user"
        self.assertEqual(["0", "0", "0", "0"], self.figures([
            use, tool_return("09:01:05", "t1", "héllo log")]))

    def test_the_index_is_read_by_its_title_line_in_both_forms_and_not_by_a_quoted_one(self) -> None:
        # The first result is the title and a newline, 55 bytes; the second is "Log: x", a CR and a
        # newline (8 bytes) and the other title and a newline (53), 61; the third quotes the title
        # inside a line and is no read of the index.
        self.assertEqual(["0", "0", "116", "2"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Bash", {"command": "cat a.md"}),
            tool_return("09:01:05", "t1", TITLE_INDEX + "\n"),
            tool_call("09:02:00", "c2", "t2", "Bash", {"command": "cat b.md"}),
            tool_return("09:02:05", "t2", "Log: x\r\n" + TITLE_SECTIONS + "\n"),
            tool_call("09:03:00", "c3", "t3", "Bash", {"command": "cat c.md"}),
            tool_return("09:03:05", "t3", "see " + TITLE_INDEX + "\n"),
        ]))

    def test_a_result_that_holds_the_index_and_a_call_that_names_the_log_count_in_both(self) -> None:
        # A command that names the log and prints the title of the index: 54 bytes and a newline.
        self.assertEqual(["55", "1", "55", "1"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Bash", {"command": "cat " + LOG + " a.md"}),
            tool_return("09:01:05", "t1", TITLE_INDEX + "\n"),
        ]))

    def test_the_log_is_named_by_any_text_of_the_input_at_any_depth(self) -> None:
        self.assertEqual(["3", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Edit", {"edits": [{"old": ["x", {"file": LOG}]}]}),
            tool_return("09:01:05", "t1", "ok."),
        ]))

    def test_a_key_that_names_the_log_and_a_value_that_does_not_are_no_read(self) -> None:
        self.assertEqual(["0", "0", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {LOG: "x", "n": 5, "ok": True, "none": None}),
            tool_return("09:01:05", "t1", "text"),
        ]))

    def test_a_lone_surrogate_in_a_result_counts_as_three_bytes_and_ends_no_run(self) -> None:
        self.assertEqual(["4", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "a" + chr(0xD800)),
        ]))

    def test_a_result_of_a_few_million_bytes_is_counted_whole(self) -> None:
        text = "é" * 1500000
        self.assertEqual(["3000000", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", text),
        ]))


class CraftedReadsTest(ReadsTestCase):
    """A transcript is untrusted input. What is no tool block is not counted and ends no run; a field
    the reading needs and the transcript lacks ends it with exit code 2 naming the file, the line
    and the field."""

    GOOD = [tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
            tool_return("09:01:05", "t1", "héllo log")]  # 10 bytes, one read

    def assert_error_names(self, entries: list[dict], field: str) -> None:
        transcript = self.session(entries)
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertNotIn("Traceback", errors)
        self.assertRegex(errors, rf"{transcript.name}:\d+: ")
        self.assertIn(field, errors)
        self.assertFalse(output.exists())

    def test_a_content_that_is_no_string_or_list_is_not_counted_and_ends_no_run(self) -> None:
        for value in (5, 1.5, True, {"type": "tool_use"}, "a string"):
            with self.subTest(content=value):
                before = tool_call("09:00:01", "b1", "tb", "Read", {"file_path": LOG})
                after = tool_return("09:00:02", "tc", "x")
                for line in (before, after):
                    line["message"]["content"] = value
                self.assertEqual(["10", "1", "0", "0"], self.figures([before, after, *self.GOOD]))

    def test_blocks_that_are_no_objects_or_no_tool_blocks_are_not_counted(self) -> None:
        junk = ["text", 5, None, True, [1, 2], {}, {"type": 7}, {"type": ["tool_use"]},
                {"type": "text", "text": LOG}, {"type": "tool_reference", "tool_name": LOG}]
        use = tool_call("09:00:01", "b1", "tb", "Read", {"file_path": LOG})
        use["message"]["content"] = junk + use["message"]["content"]
        back = tool_return("09:00:02", "tb", "bytes")
        back["message"]["content"] = junk + back["message"]["content"]
        self.assertEqual(["15", "2", "0", "0"], self.figures([use, back, *self.GOOD]))

    def test_a_result_that_is_no_text_is_a_call_that_returned_nothing_countable(self) -> None:
        # A number, a mapping and a boolean give no text, so the call is no read; a list of blocks
        # with no text block gives an empty text, which is a read of 0 bytes.
        for value, expected in ((5, ["0", "0", "0", "0"]), ({"a": LOG}, ["0", "0", "0", "0"]),
                                (True, ["0", "0", "0", "0"]),
                                ([5, "x", None, [], {"type": "text", "text": 5},
                                  {"type": ["text"], "text": "a"}, {"type": "image"}],
                                 ["0", "1", "0", "0"])):
            with self.subTest(content=value):
                self.assertEqual(expected, self.figures([
                    tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
                    tool_return("09:01:05", "t1", value)]))

    def test_an_input_that_is_a_string_a_list_or_a_number_is_searched_or_skipped(self) -> None:
        for value, expected in ((LOG, ["10", "1", "0", "0"]), ([LOG], ["10", "1", "0", "0"]),
                                (7, ["0", "0", "0", "0"]), ({}, ["0", "0", "0", "0"]),
                                ([], ["0", "0", "0", "0"]), (True, ["0", "0", "0", "0"])):
            with self.subTest(tool_input=value):
                self.assertEqual(expected, self.figures([
                    tool_call("09:01:00", "c1", "t1", "Read", value),
                    tool_return("09:01:05", "t1", "héllo log")]))

    def test_an_input_nested_3000_levels_deep_is_searched_without_a_traceback(self) -> None:
        line = json.dumps(tool_call("09:01:00", "c1", "t1", "Read", "HERE"))
        deep = "[" * 3000 + json.dumps(LOG) + "]" * 3000
        transcript = self.session([tool_return("09:01:05", "t1", "héllo log")])
        transcript.write_text(line.replace('"HERE"', deep) + "\n"
                              + json.dumps(tool_return("09:01:05", "t1", "héllo log")) + "\n",
                              encoding="utf-8")
        text = self.measures(str(transcript))
        self.assertEqual(["10", "1", "0", "0"], self.row_of(text, f"| orchestrator {SESSION} |")[-4:])

    def test_an_input_text_of_a_few_million_characters_is_searched_whole(self) -> None:
        self.assertEqual(["10", "1", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Bash", {"command": "x" * 3000000 + " " + LOG}),
            tool_return("09:01:05", "t1", "héllo log")]))

    def test_a_text_that_never_ends_a_name_is_searched_in_one_pass(self) -> None:
        # Many near matches that fail at their end: no figure, and the run ends.
        self.assertEqual(["0", "0", "0", "0"], self.figures([
            tool_call("09:01:00", "c1", "t1", "Bash", {"command": (LOG + "x ") * 200000}),
            tool_return("09:01:05", "t1", "héllo log")]))

    def test_a_missing_field_of_a_call_or_a_result_ends_with_exit_2_naming_it(self) -> None:
        for field in ("id", "name", "input"):
            with self.subTest(field=field):
                line = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
                del line["message"]["content"][0][field]
                self.assert_error_names([line], f"message.content[0].{field}")
        for field in ("tool_use_id", "content"):
            with self.subTest(field=field):
                line = tool_return("09:01:05", "t1", "x")
                del line["message"]["content"][0][field]
                self.assert_error_names([line], f"message.content[0].{field}")

    def test_a_field_that_is_null_or_no_identifier_ends_with_exit_2_naming_it(self) -> None:
        for field, value in (("id", 7), ("id", ""), ("name", ["Read"]), ("input", None)):
            with self.subTest(field=field, value=value):
                line = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
                line["message"]["content"][0][field] = value
                self.assert_error_names([line], f"message.content[0].{field}")
        for value in (["t1"], 7, None):
            with self.subTest(tool_use_id=value):
                line = tool_return("09:01:05", "t1", "x")
                line["message"]["content"][0]["tool_use_id"] = value
                self.assert_error_names([line], "message.content[0].tool_use_id")

    def test_a_line_without_its_message_or_its_content_ends_with_exit_2_naming_the_field(self) -> None:
        # The container of the blocks is a field of the reading too: its absence, or a null in its
        # place, is no empty list of blocks. An assistant line lacks `message` for `read_response`
        # before the blocks are read, so its case is the content.
        cases = [("assistant", "message.content"), ("user", "message.content"),
                 ("user", "message")]
        for kind, field in cases:
            for null in (False, True):
                with self.subTest(line=kind, field=field, null=null):
                    line = (tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
                            if kind == "assistant" else tool_return("09:01:05", "t1", "x"))
                    holder = line if field == "message" else line["message"]
                    key = field.split(".")[-1]
                    if null:
                        holder[key] = None
                    else:
                        del holder[key]
                    self.assert_error_names([line], field)

    def test_a_text_block_of_a_result_without_its_text_ends_with_exit_2_naming_the_field(self) -> None:
        for block in ({"type": "text"}, {"type": "text", "text": None}):
            with self.subTest(block=block):
                self.assert_error_names([
                    tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG}),
                    tool_return("09:01:05", "t1", [{"type": "text", "text": "a"}, block])],
                    "message.content[0].content[1].text")

    def test_the_error_of_a_missing_field_names_the_block_of_the_line(self) -> None:
        # The broken block is the second of its line, on the third line of the file.
        line = tool_call("09:01:00", "c1", "t1", "Read", {"file_path": LOG})
        line["message"]["content"].append({"type": "tool_use", "name": "Read", "input": {}})
        transcript = self.session([prompt("09:00:00", "run"), *self.GOOD[:1], line])
        code, errors = self.run_script(str(transcript), "--output", str(self.root / "o" / "m.md"))
        self.assertEqual(2, code, errors)
        self.assertIn(f"{transcript.name}:3: no field message.content[1].id", errors)

    def test_nothing_of_a_transcript_reaches_the_file_but_numbers(self) -> None:
        name = "evil|name" + chr(10) + "# injected"
        use = tool_call("09:01:00", "c1", "id|x" + chr(10) + "- injected", name, {"file_path": LOG})
        back = tool_return("09:01:05", use["message"]["content"][0]["id"], "héllo log | # injected")
        self.session([use, back])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertNotIn("injected", text)
        self.assertNotIn("evil", text)
        # "héllo log" is 10 bytes, then a space, a bar, a space, a hash, a space and "injected" (8).
        self.assertEqual(["23", "1", "0", "0"], self.row_of(text, f"| orchestrator {SESSION} |")[-4:])


class RewriteEdgesTest(MeasuresTest):
    """The rewrite of the prompt cache, one edge at a time, on orchestrators of two or three calls.
    Each call is (input, read, write)."""

    def cycle_of(self, calls: list[tuple[int, int, int]], name: str = SESSION) -> Path:
        entries = []
        for index, (input_tokens, read, write) in enumerate(calls):
            entries.append(response(f"09:{index:02d}:00", f"id{index}", input_tokens=input_tokens,
                                    read=read, write=write, output=1))
        return self.session(entries, name)

    def rewrite_lines(self, calls: list[tuple[int, int, int]]) -> tuple[str, str]:
        text = self.measures(str(self.cycle_of(calls)))
        lines = self.lines_of(text)
        return (
            next(line for line in lines if line.startswith("- Cache written again by the orchestrator: ")),
            next(line for line in lines if line.startswith("- Calls of the orchestrator with a cache write again: ")),
        )

    def test_a_rewrite_of_2000_tokens_is_not_counted(self) -> None:
        # The first call holds 2000 in the cache; the second reads none and writes 5000:
        # min(2000, 5000) = 2000, which is not above 2000.
        self.assertEqual(("- Cache written again by the orchestrator: 0",
                          "- Calls of the orchestrator with a cache write again: 0"),
                         self.rewrite_lines([(0, 0, 2000), (0, 0, 5000)]))

    def test_a_rewrite_of_2001_tokens_is_counted(self) -> None:
        self.assertEqual(("- Cache written again by the orchestrator: 2001",
                          "- Calls of the orchestrator with a cache write again: 1"),
                         self.rewrite_lines([(0, 0, 2001), (0, 0, 5000)]))

    def test_a_context_shrunk_by_exactly_30_percent_is_not_counted(self) -> None:
        # Context 10000, then 7000: 7000 * 10 = 70000 is not above 10000 * 7 = 70000, so the shrink
        # of 30% counts as a collapse of the conversation. The rewrite would be min(10000, 7000).
        self.assertEqual(("- Cache written again by the orchestrator: 0",
                          "- Calls of the orchestrator with a cache write again: 0"),
                         self.rewrite_lines([(0, 0, 10000), (0, 0, 7000)]))

    def test_a_context_shrunk_by_less_than_30_percent_is_counted(self) -> None:
        # Context 10000, then 7001: 70010 is above 70000, so the rewrite counts: min(10000, 7001).
        self.assertEqual(("- Cache written again by the orchestrator: 7001",
                          "- Calls of the orchestrator with a cache write again: 1"),
                         self.rewrite_lines([(0, 0, 10000), (0, 0, 7001)]))

    def test_the_rewrite_is_the_minimum_with_what_the_later_call_wrote(self) -> None:
        # Held 10000, read 0, so 10000 is available; the later call wrote only 3000 (context 8000,
        # not shrunk by 30%): the rewrite is 3000, not 10000.
        self.assertEqual(("- Cache written again by the orchestrator: 3000",
                          "- Calls of the orchestrator with a cache write again: 1"),
                         self.rewrite_lines([(0, 0, 10000), (5000, 0, 3000)]))

    def test_the_first_call_of_an_agent_counts_no_rewrite(self) -> None:
        self.assertEqual(("- Cache written again by the orchestrator: 0",
                          "- Calls of the orchestrator with a cache write again: 0"),
                         self.rewrite_lines([(0, 0, 50000)]))


class ShareAndBoundaryTest(MeasuresTest):
    def test_a_call_of_exactly_200000_is_not_above_and_200001_is(self) -> None:
        self.session([
            response("09:00:00", "a", write=200000, output=1),
            response("09:01:00", "b", write=200001, output=1),
        ])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        # 200001 / (200000 + 200001) = 50.00...%, one decimal half up: 50.0%.
        self.assertIn("- Share of the context in calls above 200000 tokens: 50.0%\n", text)

    def test_the_share_of_a_single_call_above_the_limit_is_100_percent(self) -> None:
        self.session([response("09:00:00", "a", write=300000, output=1)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Share of the context in calls above 200000 tokens: 100.0%\n", text)

    def test_means_round_half_up(self) -> None:
        # Contexts 1 and 2: the mean 1.5 rounds up to 2.
        self.session([
            response("09:00:00", "a", input_tokens=1, output=1),
            response("09:01:00", "b", input_tokens=2, output=1),
        ])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Mean context per call: 2\n", text)
        self.assertIn("- Mean context per call of the orchestrator: 2\n", text)

    def test_the_first_middle_and_last_call_of_an_agent(self) -> None:
        # Five calls: the middle is at position (5 - 1) // 2 = 2, the third call.
        self.session([response(f"09:0{index}:00", f"c{index}", input_tokens=(index + 1) * 10,
                               output=1) for index in range(5)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Context of the orchestrator's first call: 10\n", text)
        self.assertIn("- Context of the orchestrator's middle call: 30\n", text)
        self.assertIn("- Context of the orchestrator's last call: 50\n", text)

    def test_an_agent_with_no_calls_gives_unknown_never_zero(self) -> None:
        self.session([prompt("09:00:00", "nothing ran")])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Mean context per call of the orchestrator: unknown\n", text)
        self.assertIn("- Context of the orchestrator's first call: unknown\n", text)
        self.assertIn("- Context of the orchestrator's middle call: unknown\n", text)
        self.assertIn("- Context of the orchestrator's last call: unknown\n", text)
        self.assertIn("- Share of the context in calls above 200000 tokens: unknown\n", text)
        self.assertIn("- Calls in all: 0\n", text)


class InterleavedTest(MeasuresTest):
    """Calls of different agents, or of different sessions, that come in turn by their time."""

    def test_rewrites_are_paired_within_an_agent_when_two_agents_call_in_turn(self) -> None:
        # Orchestrator o1 09:00 writes 10000; o2 09:20 reads 0, writes 8000 (context 8000, not a
        # collapse): min(10000, 8000) = 8000 written again. Subagent s1 09:10 writes 5000; s2 09:30
        # reads 0, writes 5000: min(5000, 5000) = 5000. Pairing o1 with the call after it in time,
        # s1, would give a collapse and nothing.
        self.session([response("09:00:00", "o1", write=10000),
                      response("09:20:00", "o2", write=8000)])
        write_lines(self.project / SESSION / "subagents" / "agent-s.jsonl", [
            response("09:10:00", "s1", write=5000), response("09:30:00", "s2", write=5000)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Cache written again by the orchestrator: 8000\n", text)
        self.assertIn("- Calls of the orchestrator with a cache write again: 1\n", text)
        self.assertIn("- Cache written again by subagents: 5000\n", text)
        self.assertIn("- Calls of subagents with a cache write again: 1\n", text)

    def test_the_orchestrators_first_middle_and_last_call_over_two_sessions_are_by_time(self) -> None:
        # Session a calls at 09:00, 09:20 and 09:40 (contexts 100, 300, 500), session b at 09:10 and
        # 09:30 (200, 400). By time: 100, 200, 300, 400, 500, so the first is 100, the middle (the
        # third of five) 300 and the last 500; one session after the other would give 500 and 400.
        first = self.session([response("09:00:00", "a1", input_tokens=100),
                              response("09:20:00", "a2", input_tokens=300),
                              response("09:40:00", "a3", input_tokens=500)], "a")
        second = self.session([response("09:10:00", "b1", input_tokens=200),
                               response("09:30:00", "b2", input_tokens=400)], "b")
        text = self.measures(str(first), str(second))
        self.assertIn("- Context of the orchestrator's first call: 100\n", text)
        self.assertIn("- Context of the orchestrator's middle call: 300\n", text)
        self.assertIn("- Context of the orchestrator's last call: 500\n", text)


class ReadingErrorsTest(MeasuresTest):
    def test_a_response_without_cache_creation_ends_with_exit_2_naming_the_file_and_field(self) -> None:
        broken = response("09:00:00", "a", input_tokens=1, output=1)
        del broken["message"]["usage"]["cache_creation"]
        transcript = self.session([broken])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(transcript.name, errors)
        self.assertIn("cache_creation", errors)
        self.assertFalse(output.exists())

    def test_a_missing_five_minute_field_is_named(self) -> None:
        broken = response("09:00:00", "a", input_tokens=1, output=1)
        del broken["message"]["usage"]["cache_creation"]["ephemeral_5m_input_tokens"]
        transcript = self.session([broken])
        code, errors = self.run_script(str(transcript), "--output",
                                       str(self.root / "out" / "measures.md"))
        self.assertEqual(2, code)
        self.assertIn("ephemeral_5m_input_tokens", errors)

    def test_a_line_that_is_not_json_ends_with_exit_2_naming_the_file(self) -> None:
        transcript = self.session([prompt("09:00:00", "run")])
        with transcript.open("a", encoding="utf-8") as handle:
            handle.write("{not json\n")
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(transcript.name, errors)
        self.assertFalse(output.exists())

    def test_a_session_that_cannot_be_found_ends_with_exit_2(self) -> None:
        code, errors = self.run_script("no-such-session", "--output",
                                       str(self.root / "out" / "measures.md"))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)

    def test_no_session_named_and_no_variable_set_ends_with_exit_2(self) -> None:
        code, errors = self.run_script("--output", str(self.root / "out" / "measures.md"))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)

    def test_both_session_variables_set_ends_with_exit_2(self) -> None:
        self.session([prompt("09:00:00", "run")])
        os.environ["CLAUDE_CODE_SESSION_ID"] = SESSION
        os.environ["CODEX_SESSION_ID"] = SESSION
        code, errors = self.run_script("--output", str(self.root / "out" / "measures.md"))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)

    def test_the_session_variable_is_taken_when_no_session_is_named(self) -> None:
        self.session([response("09:00:00", "a", input_tokens=1, output=1)])
        os.environ["CLAUDE_CODE_SESSION_ID"] = SESSION
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script("--output", str(output))
        self.assertEqual(0, code, errors)
        self.assertIn("- Calls in all: 1\n", output.read_bytes().decode("utf-8"))


class EdgeReadingTest(MeasuresTest):
    def test_an_even_number_of_calls_takes_the_middle_at_position_half_minus_one(self) -> None:
        # Four calls: the middle is at (4 - 1) // 2 = 1, the second call.
        self.session([response(f"09:0{index}:00", f"c{index}", input_tokens=(index + 1) * 10,
                               output=1) for index in range(4)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Context of the orchestrator's middle call: 20\n", text)

    def test_calls_are_taken_in_the_order_of_their_time_not_of_the_lines(self) -> None:
        self.session([
            response("09:02:00", "late", input_tokens=300, output=1),
            response("09:00:00", "early", input_tokens=100, output=1),
            response("09:01:00", "middle", input_tokens=200, output=1),
        ])
        write_lines(self.project / SESSION / "subagents" / "agent-x1.jsonl", [
            response("09:02:00", "late", input_tokens=300, output=1),
            response("09:00:00", "early", input_tokens=100, output=1),
            response("09:01:00", "middle", input_tokens=200, output=1),
        ])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("- Context of the orchestrator's first call: 100\n", text)
        self.assertIn("- Context of the orchestrator's middle call: 200\n", text)
        self.assertIn("- Context of the orchestrator's last call: 300\n", text)
        self.assertIn("| x1 | Claude Code | 3 | 100 | 200 | 300 |", text)

    def test_a_response_without_message_id_ends_with_exit_2_naming_the_line_and_field(self) -> None:
        broken = response("09:00:00", "x", input_tokens=1, output=1)
        del broken["message"]["id"]
        transcript = self.session([prompt("08:59:00", "run"), broken])
        self.assert_error_names(transcript, "message.id")

    def test_a_response_without_timestamp_ends_with_exit_2_naming_the_line_and_field(self) -> None:
        broken = response("09:00:00", "x", input_tokens=1, output=1)
        del broken["timestamp"]
        transcript = self.session([prompt("08:59:00", "run"), broken])
        self.assert_error_names(transcript, "timestamp")

    def test_a_response_with_unreadable_timestamp_ends_with_exit_2_naming_the_field(self) -> None:
        broken = response("09:00:00", "x", input_tokens=1, output=1)
        broken["timestamp"] = 12345
        transcript = self.session([broken])
        self.assert_error_names(transcript, "timestamp")

    def assert_error_names(self, transcript: Path, field: str) -> None:
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(transcript.name, errors)
        self.assertIn(field, errors)
        self.assertRegex(errors, r":\d+: ")
        self.assertFalse(output.exists())

    def test_a_line_nested_too_deeply_ends_with_exit_2_naming_the_file_and_line(self) -> None:
        transcript = self.session([prompt("09:00:00", "run")])
        with transcript.open("a", encoding="utf-8") as handle:
            handle.write("[" * 200000 + "]" * 200000 + "\n")
        self.assert_error_names_line(transcript)

    def test_a_number_of_more_than_4300_digits_ends_with_exit_2_naming_the_file_and_line(self) -> None:
        transcript = self.session([prompt("09:00:00", "run")])
        digits = "9" * 5000
        with transcript.open("a", encoding="utf-8") as handle:
            handle.write('{"type": "assistant", "timestamp": "' + at("09:01:00") + '", "message": '
                         '{"id": "big", "model": "opus", "usage": {"input_tokens": ' + digits
                         + ', "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0, '
                         '"output_tokens": 1, "cache_creation": {"ephemeral_5m_input_tokens": 0, '
                         '"ephemeral_1h_input_tokens": 0}}}}\n')
        self.assert_error_names_line(transcript)

    def assert_error_names_line(self, transcript: Path) -> None:
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(transcript.name, errors)
        self.assertRegex(errors, rf"{transcript.name}:2: ")
        self.assertFalse(output.exists())

    def test_a_meta_file_with_a_number_of_more_than_4300_digits_ends_with_exit_2_naming_it(self) -> None:
        write_lines(self.project / SESSION / "subagents" / "agent-m1.jsonl", [
            response("09:00:00", "m", input_tokens=1, output=1)])
        meta = self.project / SESSION / "subagents" / "agent-m1.meta.json"
        meta.write_text('{"description": ' + "9" * 5000 + "}", encoding="utf-8")
        self.session([prompt("08:59:00", "run")])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(self.project / f"{SESSION}.jsonl"), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(meta.name, errors)
        self.assertFalse(output.exists())

    def test_a_meta_file_nested_too_deeply_ends_with_exit_2_naming_it(self) -> None:
        write_lines(self.project / SESSION / "subagents" / "agent-m1.jsonl", [
            response("09:00:00", "m", input_tokens=1, output=1)])
        meta = self.project / SESSION / "subagents" / "agent-m1.meta.json"
        meta.write_text("[" * 200000 + "]" * 200000, encoding="utf-8")
        self.session([prompt("08:59:00", "run")])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(self.project / f"{SESSION}.jsonl"), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(meta.name, errors)
        self.assertFalse(output.exists())

    def test_a_bar_and_a_control_character_in_an_agent_name_do_not_break_the_table(self) -> None:
        write_lines(self.project / SESSION / "subagents" / "agent-b1.jsonl", [
            response("09:00:00", "b", input_tokens=1, output=1)])
        (self.project / SESSION / "subagents" / "agent-b1.meta.json").write_text(json.dumps(
            {"description": "a|b\x07c", "agentType": "X"}), encoding="utf-8")
        self.session([response("09:00:00", "a", input_tokens=1, output=1)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("| a/b c (X) | Claude Code | 1 |", text)


class CodexTest(MeasuresTest):
    """Codex rollouts, written under the codex home of the run in the form Codex keeps them in."""

    def rollout(self, ident: str, entries: list[dict]) -> Path:
        return write_lines(self.root / "codex" / "sessions" / "2026" / "10" / "06"
                           / f"rollout-2026-10-06T00-00-00-{ident}.jsonl", entries)

    def assert_codex_error(self, path: Path, field: str) -> None:
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(path), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(path.name, errors)
        self.assertIn(field, errors)
        self.assertFalse(output.exists())


def codex_meta(ident: str, clock: str = "09:00:00", parent: str | None = None,
               agent_path: str | None = None, agent_nickname: str | None = None) -> dict:
    payload: dict = {"id": ident, "timestamp": at(clock)}
    if parent:
        payload["parent_thread_id"] = parent
    if agent_path:
        payload["agent_path"] = agent_path
    if agent_nickname:
        payload["agent_nickname"] = agent_nickname
    return {"timestamp": at(clock), "type": "session_meta", "payload": payload}


def codex_usage(clock: str, thread: str, input_tokens: int, cached: int = 0) -> dict:
    """A token usage record of a rollout. Its input already holds the part read from the cache."""
    return {"timestamp": at(clock), "type": "token_usage_record", "payload": {
        "thread_id": thread, "turn_id": "turn", "usage": {
            "input_tokens": input_tokens, "cached_input_tokens": cached,
            "output_tokens": 1, "total_tokens": input_tokens + 1}}}


class HandWorkedCodexTest(CodexTest):
    """A Codex orchestrator with three subagents, one of them forked, every figure worked out by hand.

    Orchestrator "orch", three calls, context = input: 1000 (of which 500 read from the cache, not
      added again), 2000, 3000. Mean 2000.
    Subagent "design", forked from orch: its rollout repeats orch's three records, which are no
      calls of design, then its own records 09:04 (6000) and 09:02 (5000), written out of time
      order. Calls in time order: 5000, 6000. Mean context 5500.
    Subagent "scout", nickname only: one call, context 400.
    Subagent "check", a subagent of design (found through design): one call, context 7.
    Rollout "other" names another parent: not in the cycle.
    Total: 7 calls, contexts summing to 17407, mean 17407 / 7 = 2486.7, rounded to 2487.
    No Codex record gives a cache write, so every cache figure is unknown.
    """

    def setUp(self) -> None:
        super().setUp()
        self.orchestrator = self.rollout("orch", [
            codex_meta("orch", "09:00:00"),
            codex_usage("09:01:00", "orch", 1000, cached=500),
            codex_usage("09:05:00", "orch", 2000),
            codex_usage("09:09:00", "orch", 3000),
        ])
        self.rollout("design", [
            codex_meta("design", "09:02:00", parent="orch", agent_path="/root/design"),
            codex_usage("09:01:00", "orch", 1000, cached=500),
            codex_usage("09:05:00", "orch", 2000),
            codex_usage("09:09:00", "orch", 3000),
            codex_usage("09:04:00", "design", 6000),
            codex_usage("09:02:00", "design", 5000),
        ])
        self.rollout("scout", [
            codex_meta("scout", "09:06:00", parent="orch", agent_nickname="scout-nick"),
            codex_usage("09:06:30", "scout", 400),
        ])
        self.rollout("check", [
            codex_meta("check", "09:03:00", parent="design", agent_path="/root/design/check"),
            codex_usage("09:03:30", "check", 7),
        ])
        self.rollout("other", [
            codex_meta("other", "09:03:00", parent="someone-else", agent_path="/root/other"),
            codex_usage("09:04:00", "other", 9999),
        ])

    def test_the_codex_figures_of_the_file_match_the_hand_worked_ones(self) -> None:
        text = self.measures(str(self.orchestrator))
        self.assertEqual([
            "# Measures of the cycle run",
            "",
            "- Calls in all: 7",
            "- Calls of the orchestrator: 3",
            "- Calls of subagents: 4",
            "- Mean context per call: 2487",
            "- Mean context per call of the orchestrator: 2000",
            "- Share of the context in calls above 200000 tokens: 0.0%",
            "- Context of the orchestrator's first call: 1000",
            "- Context of the orchestrator's middle call: 2000",
            "- Context of the orchestrator's last call: 3000",
            "- Cache written, 5 minutes: unknown",
            "- Cache written, 1 hour: unknown",
            "- Cache written again by the orchestrator: unknown",
            "- Calls of the orchestrator with a cache write again: unknown",
            "- Cache written again by subagents: unknown",
            "- Calls of subagents with a cache write again: unknown",
            "",
            "## Agents",
            "",
            "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
            "| Cache written, 1 hour | Cache written again | Calls with a cache write again "
            + NEW_COLUMNS,
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            "| orchestrator orch | Codex | 3 | 1000 | 2000 | 3000 | unknown | unknown | unknown "
            "| unknown | 0 | 0 | 0 | 0 |",
            "| /root/design | Codex | 2 | 5000 | 5000 | 6000 | unknown | unknown | unknown | unknown "
            "| 0 | 0 | 0 | 0 |",
            "| scout-nick | Codex | 1 | 400 | 400 | 400 | unknown | unknown | unknown | unknown "
            "| 0 | 0 | 0 | 0 |",
            "| /root/design/check | Codex | 1 | 7 | 7 | 7 | unknown | unknown | unknown | unknown "
            "| 0 | 0 | 0 | 0 |",
            "",
        ], self.lines_of(text))

    def test_the_forked_subagent_counts_only_its_own_calls(self) -> None:
        text = self.measures(str(self.orchestrator))
        self.assertIn("| /root/design | Codex | 2 |", text)
        self.assertIn("- Calls of subagents: 4\n", text)

    def test_a_codex_context_is_the_input_and_the_cached_part_is_not_added(self) -> None:
        text = self.measures(str(self.orchestrator))
        self.assertIn("- Context of the orchestrator's first call: 1000\n", text)


class MixedCycleTest(CodexTest):
    """A Claude Code orchestrator and a Codex orchestrator named together: the measures sum over both."""

    def test_the_measures_of_both_tools_sum_and_the_codex_cache_lines_are_unknown(self) -> None:
        claude = self.session([response("09:00:00", "a", input_tokens=100, write=1000, five=1000,
                                        output=1)], "cycle1")
        codex = self.rollout("orch", [
            codex_meta("orch", "09:00:00"),
            codex_usage("09:00:30", "orch", 300),
        ])
        text = self.measures(str(claude), str(codex))
        self.assertEqual([
            "# Measures of the cycle run",
            "",
            "- Calls in all: 2",
            "- Calls of the orchestrator: 2",
            "- Calls of subagents: 0",
            "- Mean context per call: 700",
            "- Mean context per call of the orchestrator: 700",
            "- Share of the context in calls above 200000 tokens: 0.0%",
            "- Context of the orchestrator's first call: 1100",
            "- Context of the orchestrator's middle call: 1100",
            "- Context of the orchestrator's last call: 300",
            "- Cache written, 5 minutes: unknown",
            "- Cache written, 1 hour: unknown",
            "- Cache written again by the orchestrator: unknown",
            "- Calls of the orchestrator with a cache write again: unknown",
            "- Cache written again by subagents: 0",
            "- Calls of subagents with a cache write again: 0",
            "",
            "## Agents",
            "",
            "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
            "| Cache written, 1 hour | Cache written again | Calls with a cache write again "
            + NEW_COLUMNS,
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            "| orchestrator cycle1 | Claude Code | 1 | 1100 | 1100 | 1100 | 1000 | 0 | 0 | 0 | 0 | 0 "
            "| 0 | 0 |",
            "| orchestrator orch | Codex | 1 | 300 | 300 | 300 | unknown | unknown | unknown "
            "| unknown | 0 | 0 | 0 | 0 |",
            "",
        ], self.lines_of(text))


class CodexReadingErrorsTest(CodexTest):
    def test_a_token_usage_record_without_input_tokens_ends_with_exit_2_naming_the_file_and_field(
            self) -> None:
        broken = codex_usage("09:01:00", "orch", 1000)
        del broken["payload"]["usage"]["input_tokens"]
        self.assert_codex_error(self.rollout("orch", [codex_meta("orch"), broken]), "input_tokens")

    def test_a_usage_value_that_is_no_whole_number_ends_with_exit_2_naming_the_field(self) -> None:
        broken = codex_usage("09:01:00", "orch", 1000)
        broken["payload"]["usage"]["input_tokens"] = "1000"
        self.assert_codex_error(self.rollout("orch", [codex_meta("orch"), broken]), "input_tokens")

    def test_a_session_meta_without_id_ends_with_exit_2_naming_the_field(self) -> None:
        broken = codex_meta("orch")
        del broken["payload"]["id"]
        self.assert_codex_error(self.rollout("orch", [broken]), "payload.id")

    def test_a_subagent_rollout_named_as_a_session_ends_with_exit_2(self) -> None:
        sub = self.rollout("sub", [codex_meta("sub", parent="orch", agent_path="/root/sub"),
                                   codex_usage("09:01:00", "sub", 5)])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(sub), "--output", str(output))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(sub.name, errors)
        self.assertFalse(output.exists())

    def test_a_codex_line_nested_too_deeply_ends_with_exit_2_naming_the_file_and_line(self) -> None:
        orchestrator = self.rollout("orch", [codex_meta("orch")])
        with orchestrator.open("a", encoding="utf-8") as handle:
            handle.write("[" * 200000 + "]" * 200000 + "\n")
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(orchestrator), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertRegex(errors, rf"{orchestrator.name}:2: ")
        self.assertFalse(output.exists())


def codex_item(clock: str, payload: dict) -> dict:
    """A record of a rollout that holds one item of the model's conversation."""
    return {"timestamp": at(clock), "type": "response_item", "payload": payload}


def codex_call(clock: str, call_id: str, name: str, arguments: str, custom: bool = False) -> dict:
    """The call of a tool: a function call with its arguments as a JSON text, or a custom tool call
    with its input as a text."""
    if custom:
        return codex_item(clock, {"type": "custom_tool_call", "call_id": call_id, "name": name,
                                  "input": arguments, "status": "completed"})
    return codex_item(clock, {"type": "function_call", "call_id": call_id, "name": name,
                              "arguments": arguments, "status": "completed"})


def codex_output(clock: str, call_id: str, output: object, custom: bool = False) -> dict:
    kind = "custom_tool_call_output" if custom else "function_call_output"
    return codex_item(clock, {"type": kind, "call_id": call_id, "output": output})


class CodexReadsTest(CodexTest):
    """The decision log and the index in the context of a Codex agent, read from the records of its
    tool calls and their outputs, in the form of a rollout; the content is written here."""

    def figures(self, ident: str, entries: list[dict]) -> list[str]:
        path = self.rollout(ident, [codex_meta(ident), codex_usage("09:01:00", ident, 10), *entries])
        text = self.measures(str(path))
        row = next(line for line in self.lines_of(text) if line.startswith(f"| orchestrator {ident} |"))
        return [cell.strip() for cell in row.strip("|").split("|")][-4:]

    def test_the_reads_of_a_codex_agent_and_its_subagent_have_hand_worked_figures(self) -> None:
        """The orchestrator reads the log by a function call whose arguments hold a backslash path
        (a result "héllo log": 10 bytes), by a custom tool call (an output of two text blocks, "ab"
        and "cé", and an image: 5 bytes), and by arguments that are no JSON (1 byte), and reads the
        list of sections by a command (53 bytes). Its subagent reads the log (3 bytes)."""
        path = self.rollout("orch", [
            codex_meta("orch"),
            codex_usage("09:01:00", "orch", 10),
            codex_call("09:02:00", "k1", "shell", json.dumps(
                {"command": "cat .the-way" + chr(92) + "foundations" + chr(92) + "decisions.md"})),
            codex_output("09:02:05", "k1", "héllo log"),
            codex_call("09:03:00", "k2", "exec", "tools.read('foundations/decisions.md')", True),
            codex_output("09:03:05", "k2", [{"type": "input_text", "text": "ab"},
                                            {"type": "input_image", "image_url": "u", "detail": "low"},
                                            {"type": "input_text", "text": "cé"}], True),
            codex_call("09:04:00", "k3", "wait", "not JSON: foundations/decisions.md"),
            codex_output("09:04:05", "k3", "q"),
            codex_call("09:05:00", "k4", "shell", json.dumps({"command": "cat sections.md"})),
            codex_output("09:05:05", "k4", "# decision_index.py: list of the sections of the log\n"),
            codex_call("09:06:00", "k5", "shell", json.dumps({"command": "ls foundations"})),
            codex_output("09:06:05", "k5", "decisions.md"),
            codex_output("09:07:05", "ghost", "no call of this agent has this id"),
        ])
        self.rollout("scout", [
            codex_meta("scout", "09:02:00", parent="orch", agent_nickname="scout"),
            codex_usage("09:02:30", "scout", 5),
            codex_call("09:03:00", "k1", "shell", json.dumps({"command": "cat foundations/decisions.md"})),
            codex_output("09:03:05", "k1", "xyz"),
        ])
        text = self.measures(str(path))
        self.assertEqual(["16", "3", "53", "1"],
                         [cell.strip() for cell in next(line for line in self.lines_of(text) if
                                                         line.startswith("| orchestrator orch |")
                                                         ).strip("|").split("|")][-4:])
        self.assertEqual(["3", "1", "0", "0"],
                         [cell.strip() for cell in next(line for line in self.lines_of(text) if
                                                         line.startswith("| scout |")
                                                         ).strip("|").split("|")][-4:])

    def test_a_record_that_is_no_tool_record_is_not_counted(self) -> None:
        self.assertEqual(["0", "0", "0", "0"], self.figures("orch", [
            codex_item("09:02:00", {"type": "message", "role": "user", "content": [
                {"type": "input_text", "text": "foundations/decisions.md"}]}),
            codex_item("09:02:01", "not an object"),
            codex_item("09:02:02", {"type": "reasoning"}),
            codex_item("09:02:03", {"type": ["function_call"]}),
            codex_output("09:02:05", "k1", "foundations/decisions.md"),
            codex_call("09:03:00", "k2", "shell", json.dumps({"command": "cat foundations/decisions.md"})),
        ]))

    def test_an_output_that_is_no_text_is_not_counted(self) -> None:
        for value in (5, {"text": "a"}, None):
            with self.subTest(output=value):
                if value is None:
                    continue  # a missing output is an error, tested below
                self.assertEqual(["0", "0", "0", "0"], self.figures("orch", [
                    codex_call("09:02:00", "k1", "shell",
                               json.dumps({"command": "cat foundations/decisions.md"})),
                    codex_output("09:02:05", "k1", value)]))

    def test_a_response_item_without_its_payload_ends_with_exit_2_naming_the_field(self) -> None:
        for null in (False, True):
            with self.subTest(null=null):
                record = codex_call("09:02:00", "k1", "shell", "{}")
                if null:
                    record["payload"] = None
                else:
                    del record["payload"]
                self.assert_codex_error(self.rollout("orch", [codex_meta("orch"), record]), "payload")

    def test_a_text_block_of_an_output_without_its_text_ends_with_exit_2_naming_the_field(self) -> None:
        output = [{"type": "input_text", "text": "a"}, {"type": "input_text"}]
        self.assert_codex_error(self.rollout("orch", [
            codex_meta("orch"), codex_call("09:02:00", "k1", "shell", "{}"),
            codex_output("09:02:05", "k1", output)]), "payload.output[1].text")

    def test_a_missing_field_of_a_call_or_an_output_ends_with_exit_2_naming_it(self) -> None:
        cases = [
            ("payload.call_id", codex_call("09:02:00", "k1", "shell", "{}"), "call_id"),
            ("payload.name", codex_call("09:02:00", "k1", "shell", "{}"), "name"),
            ("payload.arguments", codex_call("09:02:00", "k1", "shell", "{}"), "arguments"),
            ("payload.input", codex_call("09:02:00", "k1", "exec", "x", True), "input"),
            ("payload.call_id", codex_output("09:02:05", "k1", "x"), "call_id"),
            ("payload.output", codex_output("09:02:05", "k1", "x"), "output"),
        ]
        for label, record, key in cases:
            with self.subTest(field=label, record=record["payload"]["type"]):
                del record["payload"][key]
                self.assert_codex_error(self.rollout("orch", [codex_meta("orch"), record]), label)


class CodexSearchTest(CodexTest):
    """The search of a Codex orchestrator's subagents among the rollouts under the codex home."""

    def setUp(self) -> None:
        super().setUp()
        # The orchestrator's first call is at 09:01 on 2026-10-06 (UTC).
        self.orchestrator = self.rollout("orch", [codex_meta("orch", "09:00:00"),
                                                  codex_usage("09:01:00", "orch", 1000)])
        self.floor = datetime(2026, 10, 6, 9, 1, tzinfo=timezone.utc).timestamp()

    def unreadable(self, ident: str, modified: float) -> Path:
        path = self.root / "codex" / "sessions" / "2026" / "09" / f"rollout-{ident}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("this is not JSON\n", encoding="utf-8")
        os.utime(path, (modified, modified))
        return path

    def test_a_rollout_older_than_the_orchestrators_first_call_is_not_read(self) -> None:
        self.unreadable("stale", self.floor - 3600)
        text = self.measures(str(self.orchestrator))
        self.assertIn("- Calls in all: 1\n", text)

    def test_a_newer_rollout_with_an_unreadable_first_line_is_loud(self) -> None:
        bad = self.unreadable("fresh", self.floor + 3600)
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(self.orchestrator), "--output", str(output))
        self.assertEqual(2, code, errors)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertIn(bad.name, errors)
        self.assertFalse(output.exists())

    def test_a_second_rollout_with_an_id_already_found_is_left_out_with_a_warning(self) -> None:
        self.rollout("dup", [codex_meta("dup", "09:02:00", parent="orch", agent_path="/root/dup"),
                             codex_usage("09:02:30", "dup", 50)])
        copy = write_lines(self.root / "codex" / "sessions" / "2026" / "10" / "07"
                           / "rollout-2026-10-07T00-00-00-dup.jsonl",
                           [codex_meta("dup", "09:02:00", parent="orch", agent_path="/root/dup"),
                            codex_usage("09:02:30", "dup", 50), codex_usage("09:03:30", "dup", 60)])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(self.orchestrator), "--output", str(output))
        self.assertEqual(0, code, errors)
        self.assertNotIn("Error:", errors)
        self.assertIn("Warning: ", errors)
        self.assertIn(copy.name, errors)
        text = output.read_bytes().decode("utf-8")
        self.assertIn("- Calls of subagents: 1\n", text)
        self.assertIn("| /root/dup | Codex | 1 | 50 |", text)


class ScriptTest(unittest.TestCase):
    def test_the_script_imports_only_the_standard_library(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        modules: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                if node.level:
                    modules.add("<relative import>")
                elif node.module:
                    modules.add(node.module.split(".")[0])
        self.assertTrue(modules <= set(sys.stdlib_module_names),
                        f"not standard library: {sorted(modules - set(sys.stdlib_module_names))}")


if __name__ == "__main__":
    unittest.main()
