"""Tests of task-cycle/cycle_measures.py on small transcripts in the form Claude Code keeps them in.

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
            "| Cache written, 1 hour | Cache written again | Calls with a cache write again |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            f"| orchestrator {SESSION} | Claude Code | 3 | 1100 | 4105 | 4203 | 5000 | 3000 | 3900 | 1 |",
            "| implement task 1 (general-purpose) | Claude Code | 3 | 510 | 2901 | 4502 | 4500 "
            "| 2500 | 2400 | 1 |",
            "| a2 | Claude Code | 1 | 301 | 301 | 301 | 300 | 0 | 0 | 0 |",
            "| nested check (Explore) | Claude Code | 1 | 10 | 10 | 10 | 0 | 0 | 0 | 0 |",
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
        self.assert_error_names(transcript, 2, "message.id")

    def test_a_response_without_timestamp_ends_with_exit_2_naming_the_line_and_field(self) -> None:
        broken = response("09:00:00", "x", input_tokens=1, output=1)
        del broken["timestamp"]
        transcript = self.session([prompt("08:59:00", "run"), broken])
        self.assert_error_names(transcript, 2, "timestamp")

    def test_a_response_with_unreadable_timestamp_ends_with_exit_2_naming_the_field(self) -> None:
        broken = response("09:00:00", "x", input_tokens=1, output=1)
        broken["timestamp"] = 12345
        transcript = self.session([broken])
        self.assert_error_names(transcript, 2, "timestamp")

    def assert_error_names(self, transcript: Path, code_expected: int, field: str) -> None:
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(transcript), "--output", str(output))
        self.assertEqual(code_expected, code, errors)
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

    def test_a_bar_and_a_control_character_in_an_agent_name_do_not_break_the_table(self) -> None:
        write_lines(self.project / SESSION / "subagents" / "agent-b1.jsonl", [
            response("09:00:00", "b", input_tokens=1, output=1)])
        (self.project / SESSION / "subagents" / "agent-b1.meta.json").write_text(json.dumps(
            {"description": "a|b\x07c", "agentType": "X"}), encoding="utf-8")
        self.session([response("09:00:00", "a", input_tokens=1, output=1)])
        text = self.measures(str(self.project / f"{SESSION}.jsonl"))
        self.assertIn("| a/b c (X) | Claude Code | 1 |", text)

    def test_a_codex_rollout_is_refused_with_exit_2(self) -> None:
        rollout = write_lines(self.root / "rollout-x.jsonl", [
            {"timestamp": at("09:00:00"), "type": "session_meta", "payload": {"id": "x"}}])
        output = self.root / "out" / "measures.md"
        code, errors = self.run_script(str(rollout), "--output", str(output))
        self.assertEqual(2, code)
        self.assertTrue(errors.startswith("Error: "), errors)
        self.assertFalse(output.exists())


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
