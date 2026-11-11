"""Tests of task-cycle/cycle_stages.py on small transcripts in the form Codex and Claude Code keep
them in."""

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cycle_stages  # noqa: E402

DAY = "2026-10-06T"


def at(clock: str) -> str:
    return f"{DAY}{clock}.000Z"


def write_lines(path: Path, entries: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(entry) + "\n" for entry in entries), encoding="utf-8")
    return path


# Codex


def meta(ident: str, clock: str, parent: str | None = None, agent_path: str | None = None) -> dict:
    payload = {"id": ident, "timestamp": at(clock)}
    if parent:
        payload.update(parent_thread_id=parent, agent_path=agent_path)
    return {"timestamp": at(clock), "type": "session_meta", "payload": payload}


def started(clock: str, turn: str) -> dict:
    return {"timestamp": at(clock), "type": "event_msg",
            "payload": {"type": "task_started", "turn_id": turn}}


def complete(clock: str, turn: str) -> dict:
    return {"timestamp": at(clock), "type": "event_msg",
            "payload": {"type": "task_complete", "turn_id": turn}}


def context(clock: str, turn: str, model: str) -> dict:
    return {"timestamp": at(clock), "type": "turn_context",
            "payload": {"turn_id": turn, "model": model}}


def tokens(clock: str, thread: str, turn: str, total_input: int, cached: int, output: int) -> dict:
    return {"timestamp": at(clock), "type": "token_usage_record", "payload": {
        "thread_id": thread, "turn_id": turn, "usage": {
            "input_tokens": total_input, "cached_input_tokens": cached,
            "output_tokens": output, "total_tokens": total_input + output}}}


def rollout(home: Path, ident: str, entries: list[dict]) -> Path:
    return write_lines(home / "sessions" / "2026" / "10" / "06"
                       / f"rollout-2026-10-06T00-00-00-{ident}.jsonl", entries)


def find(rows: list[cycle_stages.Row], name: str) -> cycle_stages.Row:
    matches = [row for row in rows if row.name == name]
    if len(matches) != 1:
        raise AssertionError(f"{len(matches)} rows named {name!r}: {[r.name for r in rows]}")
    return matches[0]


class CodexTest(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "codex"
        self.orchestrator = rollout(self.home, "orch", [
            meta("orch", "10:00:00"),
            started("10:00:00", "o1"),
            context("10:00:00", "o1", "model-o"),
            tokens("10:01:00", "orch", "o1", 100, 40, 10),   # before any subagent
            tokens("10:03:00", "orch", "o1", 200, 50, 20),   # while design runs alone
            tokens("10:06:00", "orch", "o1", 300, 60, 30),   # between design and its follow-up
            tokens("10:09:00", "orch", "o1", 400, 70, 40),   # while design and planner both run
            complete("10:20:00", "o1"),
        ])
        # A forked subagent's rollout starts with a copy of its parent's history.
        rollout(self.home, "design", [
            meta("design", "10:02:00", "orch", "/root/design"),
            meta("orch", "10:00:00"),
            started("10:02:00", "o1"),
            started("10:02:00", "d1"),
            context("10:02:00", "d1", "model-d"),
            tokens("10:04:00", "design", "d1", 1000, 900, 100),
            complete("10:05:00", "d1"),
            started("10:08:00", "d2"),
            context("10:08:00", "d2", "model-d"),
            tokens("10:09:30", "design", "d2", 2000, 1800, 200),
            complete("10:10:00", "d2"),
        ])
        rollout(self.home, "planner", [
            meta("planner", "10:08:30", "orch", "/root/planner"),
            started("10:08:30", "p1"),
            context("10:08:30", "p1", "model-p"),
            tokens("10:11:00", "planner", "p1", 3000, 2000, 300),
            complete("10:12:00", "p1"),
        ])
        # A subagent of the planner counts towards the planner's stage.
        rollout(self.home, "helper", [
            meta("helper", "10:09:00", "planner", "/root/planner/helper"),
            started("10:09:00", "h1"),
            context("10:09:00", "h1", "model-h"),
            tokens("10:10:00", "helper", "h1", 5000, 4000, 500),
            complete("10:10:30", "h1"),
        ])
        # Another session's subagent is not this cycle's.
        rollout(self.home, "other", [
            meta("other", "10:03:00", "someone-else", "/root/other"),
            started("10:03:00", "x1"),
            tokens("10:04:00", "other", "x1", 9999, 0, 9),
            complete("10:05:00", "x1"),
        ])

    def tearDown(self) -> None:
        self.folder.cleanup()

    def rows(self) -> list[cycle_stages.Row]:
        session = cycle_stages.read_session(self.orchestrator, self.home)
        return cycle_stages.build_rows([session])

    def test_each_subagent_turn_is_a_stage_with_its_own_tokens_and_model(self) -> None:
        rows = self.rows()
        first = find(rows, "/root/design — turn 1")
        self.assertEqual(first.duration.total_seconds(), 180)
        self.assertEqual(first.subagent.total, 1100)
        self.assertEqual(first.subagent_models, ["model-d"])
        second = find(rows, "/root/design — turn 2")
        self.assertEqual(second.subagent.total, 2200)

    def test_a_forked_rollout_gives_no_turn_of_its_parent(self) -> None:
        names = [row.name for row in self.rows()]
        self.assertNotIn("/root/design — turn 3", names)
        self.assertIn("/root/design — turn 1", names)

    def test_a_nested_subagent_counts_towards_its_top_level_stage(self) -> None:
        planner = find(self.rows(), "/root/planner")
        self.assertEqual(planner.subagent.total, 3300 + 5500)
        self.assertEqual(planner.subagent_models, ["model-h", "model-p"])

    def test_another_sessions_subagent_is_left_out(self) -> None:
        rows = self.rows()
        self.assertFalse(any("/root/other" in row.name for row in rows))
        self.assertNotIn(9999 + 9, [row.subagent.total for row in rows])

    def test_orchestrator_tokens_go_to_the_stage_then_running(self) -> None:
        rows = self.rows()
        self.assertEqual(find(rows, "/root/design — turn 1").orchestrator.total, 220)
        self.assertEqual(find(rows, "/root/design — turn 1").orchestrator_models, ["model-o"])
        stretches = [row for row in rows if row.name == "orchestrator"]
        self.assertEqual([row.orchestrator.total for row in stretches], [110, 330, 0])

    def test_orchestrator_tokens_while_turns_overlap_stand_apart(self) -> None:
        row = find(self.rows(), "orchestrator while in parallel: "
                                "/root/design — turn 2, /root/planner")
        self.assertEqual(row.orchestrator.total, 440)
        self.assertIsNone(row.duration)

    def test_an_orchestrator_stretch_lasts_only_outside_subagent_turns(self) -> None:
        stretches = [row for row in self.rows() if row.name == "orchestrator"]
        # 10:00-10:02, 10:05-10:08 and 10:12-10:20.
        self.assertEqual([row.duration.total_seconds() for row in stretches], [120, 180, 480])

    def test_rows_stand_in_time_order(self) -> None:
        names = [row.name for row in self.rows()]
        self.assertEqual(names, [
            "orchestrator", "/root/design — turn 1", "orchestrator", "/root/design — turn 2",
            "/root/planner", "orchestrator while in parallel: /root/design — turn 2, "
            "/root/planner", "orchestrator"])

    def test_every_token_is_counted_once(self) -> None:
        rows = self.rows()
        counted = sum(row.subagent.total + row.orchestrator.total for row in rows)
        self.assertEqual(counted, 1100 + 2200 + 3300 + 5500 + 110 + 220 + 330 + 440)

    def test_transcripts_read_as_written_give_no_warning(self) -> None:
        session = cycle_stages.read_session(self.orchestrator, self.home)
        self.assertEqual(cycle_stages.find_warnings([session]), [])

    def test_a_subagent_turn_without_its_end_is_reported(self) -> None:
        rollout(self.home, "stuck", [
            meta("stuck", "10:13:00", "orch", "/root/stuck"),
            started("10:13:00", "s1"),
            context("10:13:00", "s1", "model-s"),
            tokens("10:14:00", "stuck", "s1", 10, 0, 1),
        ])
        session = cycle_stages.read_session(self.orchestrator, self.home)
        self.assertEqual(cycle_stages.find_warnings([session]), [
            "Codex session `orch`, /root/stuck: 1 turn(s) without `task_complete`, each ending "
            "at its last entry"])

    def test_a_transcript_whose_lines_are_not_recognised_is_reported(self) -> None:
        # Lines of a layout the reader does not know: no turn and no usage is found.
        rollout(self.home, "renamed", [
            meta("renamed", "10:13:00", "orch", "/root/renamed"),
            {"timestamp": at("10:14:00"), "type": "usage", "payload": {"thread_id": "renamed"}},
        ])
        session = cycle_stages.read_session(self.orchestrator, self.home)
        self.assertEqual(cycle_stages.find_warnings([session]), [
            "Codex session `orch`, /root/renamed: no turn found",
            "Codex session `orch`, /root/renamed: no token usage found"])

    def test_a_session_is_found_by_its_id(self) -> None:
        path = cycle_stages.resolve("orch", self.home, Path(self.folder.name) / "claude")
        self.assertEqual(path, self.orchestrator)

    def test_a_subagent_rollout_is_refused_as_the_orchestrator(self) -> None:
        path = cycle_stages.resolve("design", self.home, Path(self.folder.name) / "claude")
        with self.assertRaisesRegex(cycle_stages.CycleStagesError, "subagent"):
            cycle_stages.read_session(path, self.home)


# Claude Code


def prompt(clock: str, text: str, meta_line: bool = False) -> dict:
    entry = {"type": "user", "timestamp": at(clock),
             "message": {"role": "user", "content": text}}
    if meta_line:
        entry["isMeta"] = True
    return entry


def result(clock: str) -> dict:
    return {"type": "user", "timestamp": at(clock), "message": {
        "role": "user", "content": [{"type": "tool_result", "tool_use_id": "t", "content": "ok"}]}}


def answer(clock: str, ident: str, model: str, uncached: int, written: int, read: int,
           output: int, stop: str | None) -> dict:
    return {"type": "assistant", "timestamp": at(clock), "message": {
        "id": ident, "model": model, "stop_reason": stop, "content": [{"type": "text"}],
        "usage": {"input_tokens": uncached, "cache_creation_input_tokens": written,
                  "cache_read_input_tokens": read, "output_tokens": output}}}


class ClaudeCodeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "claude"
        project = self.home / "projects" / "C--repo"
        self.main = write_lines(project / "sess.jsonl", [
            prompt("09:00:00", "run the cycle"),
            # One response written over three lines that repeat its usage.
            answer("09:00:10", "m1", "opus", 10, 100, 1000, 2, None),
            answer("09:00:11", "m1", "opus", 10, 100, 1000, 2, None),
            answer("09:00:20", "m1", "opus", 10, 100, 1000, 50, "tool_use"),
            prompt("09:00:21", "Base directory for this skill: ...", meta_line=True),
            result("09:00:30"),
            answer("09:00:50", "m2", "opus", 1, 0, 500, 5, "end_turn"),
            # The orchestrator waits; a notice of the finished subagent wakes it.
            prompt("09:20:00", "<task-notification>done</task-notification>"),
            answer("09:20:30", "m3", "opus", 1, 0, 600, 6, "end_turn"),
            # An hour for the human, then a short turn.
            prompt("10:30:00", "ok"),
            answer("10:31:00", "m4", "opus", 1, 0, 700, 7, "end_turn"),
        ])
        agents = project / "sess" / "subagents"
        write_lines(agents / "agent-a1.jsonl", [
            prompt("09:01:00", "implement task 1"),
            answer("09:05:00", "s1", "sonnet", 3, 30, 300, 3, "tool_use"),
            prompt("09:05:01", "Base directory for this skill: ...", meta_line=True),
            answer("09:10:00", "s2", "sonnet", 4, 40, 400, 4, "end_turn"),
            # The coordinator resumes the finished agent.
            prompt("09:15:00", "The coordinator sent a message: fix it", meta_line=True),
            answer("09:18:00", "s3", "sonnet", 5, 50, 500, 5, "end_turn"),
        ])
        (agents / "agent-a1.meta.json").write_text(json.dumps(
            {"agentType": "general-purpose", "description": "Implement Task 1"}), "utf-8")
        write_lines(agents / "agent-a2.jsonl", [
            prompt("09:06:00", "review"),
            answer("09:07:00", "n1", "haiku", 7, 70, 700, 7, "end_turn"),
        ])
        (agents / "agent-a2.meta.json").write_text(json.dumps(
            {"agentType": "general-purpose", "description": "nested review",
             "parentAgentId": "a1"}), "utf-8")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def rows(self) -> list[cycle_stages.Row]:
        path = cycle_stages.resolve("sess", Path(self.folder.name) / "codex", self.home)
        session = cycle_stages.read_session(path, Path(self.folder.name) / "codex")
        return cycle_stages.build_rows([session])

    def test_a_response_written_over_several_lines_counts_once(self) -> None:
        first = self.rows()[0]
        self.assertEqual(first.name, "orchestrator")
        self.assertEqual(first.orchestrator.input, 1110 + 501)
        self.assertEqual(first.orchestrator.cached, 1000 + 500)
        self.assertEqual(first.orchestrator.output, 55)

    def test_a_coordinator_message_after_the_answer_starts_a_new_turn(self) -> None:
        rows = self.rows()
        first = find(rows, "Implement Task 1 (general-purpose) — turn 1")
        self.assertEqual(first.duration.total_seconds(), 9 * 60)
        second = find(rows, "Implement Task 1 (general-purpose) — turn 2")
        self.assertEqual(second.duration.total_seconds(), 3 * 60)

    def test_a_nested_subagent_counts_towards_its_top_level_stage(self) -> None:
        rows = self.rows()
        self.assertFalse(any("nested review" in row.name for row in rows))
        first = find(rows, "Implement Task 1 (general-purpose) — turn 1")
        self.assertEqual(first.subagent.total, (333 + 3) + (444 + 4) + (777 + 7))
        self.assertEqual(first.subagent_models, ["sonnet", "haiku"])

    def test_the_wait_for_the_human_is_left_out(self) -> None:
        stretches = [row for row in self.rows() if row.name == "orchestrator"]
        # 09:00:00-09:00:50 before the subagent; after it 09:20:00-09:20:30 and 10:30-10:31.
        self.assertEqual([row.duration.total_seconds() for row in stretches], [50, 90])

    def test_the_report_holds_every_stage_and_the_totals(self) -> None:
        output = Path(self.folder.name) / "out" / "stages.md"
        code = cycle_stages.main(["sess", "--claude-home", str(self.home),
                                  "--codex-home", str(Path(self.folder.name) / "codex"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        text = output.read_text(encoding="utf-8")
        self.assertIn("| Implement Task 1 (general-purpose) — turn 2 | 0:03:00 | sonnet | — |",
                      text)
        total = (1110 + 50) + (501 + 5) + (601 + 6) + (701 + 7) + 336 + 448 + 784 + 560
        self.assertIn(f"- Tokens in all: {total:,}", text)
        self.assertIn("| haiku | 784 |", text)
        self.assertIn("- Claude Code session `sess`: 2 subagents — `sess.jsonl`", text)

    def test_a_subagent_without_its_meta_file_is_reported(self) -> None:
        (self.home / "projects" / "C--repo" / "sess" / "subagents" / "agent-a2.meta.json").unlink()
        path = cycle_stages.resolve("sess", Path(self.folder.name) / "codex", self.home)
        session = cycle_stages.read_session(path, Path(self.folder.name) / "codex")
        self.assertEqual(cycle_stages.find_warnings([session]), [
            "Claude Code session `sess`, a2: no `agent-a2.meta.json`, so it is named by its id"])

    def test_warnings_stand_in_the_report_and_on_stderr(self) -> None:
        write_lines(self.home / "projects" / "C--repo" / "sess" / "subagents"
                    / "agent-a3.jsonl", [prompt("09:30:00", "idle")])
        output = Path(self.folder.name) / "out" / "warned.md"
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = cycle_stages.main(["sess", "--claude-home", str(self.home),
                                      "--codex-home", str(Path(self.folder.name) / "codex"),
                                      "--output", str(output)])
        self.assertEqual(code, 0)
        warning = "Claude Code session `sess`, a3: no turn found"
        self.assertIn(f"Warning: {warning}", stderr.getvalue())
        self.assertIn(f"Warnings:\n- {warning}\n", output.read_text(encoding="utf-8"))

    def test_a_session_named_twice_counts_once(self) -> None:
        output = Path(self.folder.name) / "out" / "twice.md"
        transcript = self.home / "projects" / "C--repo" / "sess.jsonl"
        code = cycle_stages.main(["sess", str(transcript), "--claude-home", str(self.home),
                                  "--codex-home", str(Path(self.folder.name) / "codex"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        self.assertEqual(output.read_text(encoding="utf-8").count("Claude Code session"), 1)


def tool_answer(clock: str, ident: str, model: str, uncached: int, written: int, read: int,
                output: int, call: str, name: str) -> dict:
    """A response whose content is one tool call."""
    entry = answer(clock, ident, model, uncached, written, read, output, "tool_use")
    entry["message"]["content"] = [{"type": "tool_use", "id": call, "name": name, "input": {}}]
    return entry


def call_result(clock: str, call: str) -> dict:
    return {"type": "user", "timestamp": at(clock), "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": call, "content": "ok"}]}}


class ClaudeWaitTest(unittest.TestCase):
    """A stage with one Bash call (15 s) and one SendMessage call of the orchestrator (1 s) that
    must not count as a wait for a tool."""

    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "claude"
        project = self.home / "projects" / "C--repo"
        write_lines(project / "wait.jsonl", [
            prompt("09:00:00", "run the cycle"),
            tool_answer("09:00:05", "o1", "opus", 1, 0, 100, 1, "ag1", "Agent"),
            call_result("09:00:06", "ag1"),
            tool_answer("09:00:30", "o2", "opus", 1, 0, 100, 1, "sm1", "SendMessage"),
            call_result("09:00:31", "sm1"),
            answer("09:00:45", "o3", "opus", 1, 0, 100, 1, "end_turn"),
        ])
        agents = project / "wait" / "subagents"
        write_lines(agents / "agent-s1.jsonl", [
            prompt("09:00:06", "implement"),
            tool_answer("09:00:10", "x1", "sonnet", 3, 30, 300, 3, "b1", "Bash"),
            call_result("09:00:25", "b1"),
            answer("09:00:40", "x2", "sonnet", 4, 40, 400, 4, "end_turn"),
        ])
        (agents / "agent-s1.meta.json").write_text(json.dumps(
            {"agentType": "general-purpose", "description": "Implement"}), "utf-8")
        write_lines(project / "lost.jsonl", [
            prompt("09:00:00", "run"),
            tool_answer("09:00:10", "o1", "opus", 1, 0, 100, 1, "lost1", "Bash"),
            answer("09:00:20", "o2", "opus", 1, 0, 100, 1, "end_turn"),
        ])

    def tearDown(self) -> None:
        self.folder.cleanup()

    def report(self, session: str) -> str:
        output = Path(self.folder.name) / "out" / f"{session}.md"
        code = cycle_stages.main([session, "--claude-home", str(self.home),
                                  "--codex-home", str(Path(self.folder.name) / "codex"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        return output.read_text(encoding="utf-8")

    def test_a_tool_call_counts_as_a_wait_and_a_subagent_message_does_not(self) -> None:
        text = self.report("wait")
        self.assertIn("| Implement (general-purpose) | 2026-10-06 09:00:06 | 0:00:15 | sonnet "
                      "| 777 | 700 | 7 |", text)

    def test_the_summary_splits_working_time_into_waiting_and_the_rest(self) -> None:
        text = self.report("wait")
        self.assertIn("- Working time, orchestrator turns and subagent turns joined: 0:00:45", text)
        self.assertIn("- Waiting for tools: 0:00:15", text)
        self.assertIn("- Working time without waiting for tools: 0:00:30", text)

    def test_a_call_without_its_result_makes_the_wait_unknown_and_is_warned(self) -> None:
        text = self.report("lost")
        self.assertIn("- Waiting for tools: unknown", text)
        self.assertIn("| unknown (at least 0:00:00) | opus |", text)
        self.assertIn("- Claude Code session `lost`, the orchestrator: 1 tool call(s) with no "
                      "readable result: their waits are unknown", text)

    def live(self, *last: dict) -> str:
        """The report of a session whose transcript ends with `last`, as the transcript of the
        session running this script ends while the call that runs it waits for its result."""
        write_lines(self.home / "projects" / "C--repo" / "live.jsonl", [
            prompt("09:00:00", "run the cycle"),
            tool_answer("09:00:10", "o1", "opus", 1, 0, 100, 1, "b1", "Bash"),
            call_result("09:00:25", "b1"),
            *last,
        ])
        return self.report("live")

    def test_a_call_the_transcript_ends_in_is_no_wait_and_no_unknown(self) -> None:
        text = self.live(tool_answer("09:00:40", "o2", "opus", 1, 0, 100, 1, "run", "Bash"))
        self.assertIn("- Waiting for tools: 0:00:15", text)
        self.assertIn("- Working time without waiting for tools: 0:00:25", text)
        self.assertIn("Warnings: none.", text)

    def test_parallel_calls_of_the_last_response_are_no_wait_and_no_unknown(self) -> None:
        # One response written over two lines, each with one of its calls.
        text = self.live(tool_answer("09:00:40", "o2", "opus", 1, 0, 100, 1, "run", "Bash"),
                         tool_answer("09:00:41", "o2", "opus", 1, 0, 100, 1, "read", "Read"))
        self.assertIn("- Waiting for tools: 0:00:15", text)
        self.assertIn("Warnings: none.", text)

    def test_a_call_without_its_result_before_a_later_entry_stays_unknown(self) -> None:
        for label, later in (
                ("a later result", call_result("09:00:50", "other")),
                ("a later message", prompt("09:00:50", "go on")),
                ("a later response", answer("09:00:50", "o3", "opus", 1, 0, 100, 1, "end_turn"))):
            with self.subTest(label):
                text = self.live(tool_answer("09:00:40", "o2", "opus", 1, 0, 100, 1, "run",
                                             "Bash"), later)
                self.assertIn("- Waiting for tools: unknown", text)
                self.assertIn("1 tool call(s) with no readable result", text)


def codex_call(clock: str, name: str, ident: str) -> dict:
    return {"timestamp": at(clock), "type": "response_item", "payload": {
        "type": "function_call", "name": name, "call_id": ident, "arguments": "{}"}}


def codex_call_output(clock: str, ident: str) -> dict:
    return {"timestamp": at(clock), "type": "response_item", "payload": {
        "type": "function_call_output", "call_id": ident, "output": "ok"}}


class CodexWaitTest(unittest.TestCase):
    """A stage with one shell call (15 s); spawn_agent, send_message and wait_agent are subagent
    calls and no wait for a tool."""

    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "codex"
        rollout(self.home, "orchw", [
            meta("orchw", "10:00:00"),
            started("10:00:00", "o1"),
            context("10:00:00", "o1", "model-o"),
            codex_call("10:00:05", "spawn_agent", "c-spawn"),
            codex_call_output("10:00:06", "c-spawn"),
            codex_call("10:00:20", "send_message", "c-msg"),
            codex_call_output("10:00:21", "c-msg"),
            codex_call("10:00:41", "wait_agent", "c-wait"),
            codex_call_output("10:00:50", "c-wait"),
            tokens("10:00:30", "orchw", "o1", 100, 0, 10),
            complete("10:01:00", "o1"),
        ])
        rollout(self.home, "work", [
            meta("work", "10:00:06", "orchw", "/root/work"),
            started("10:00:06", "w1"),
            context("10:00:06", "w1", "model-w"),
            codex_call("10:00:10", "shell", "c-shell"),
            codex_call_output("10:00:25", "c-shell"),
            tokens("10:00:30", "work", "w1", 500, 200, 20),
            complete("10:00:40", "w1"),
        ])

    def tearDown(self) -> None:
        self.folder.cleanup()

    def report(self, session: str) -> str:
        output = Path(self.folder.name) / "out" / f"{session}.md"
        code = cycle_stages.main([session, "--codex-home", str(self.home),
                                  "--claude-home", str(Path(self.folder.name) / "claude"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        return output.read_text(encoding="utf-8")

    def test_a_tool_call_counts_as_a_wait_and_subagent_calls_do_not(self) -> None:
        text = self.report("orchw")
        self.assertIn("| /root/work | 2026-10-06 10:00:06 | 0:00:15 | model-w | 500 | 200 | 20 |",
                      text)

    def test_the_summary_splits_working_time_into_waiting_and_the_rest(self) -> None:
        text = self.report("orchw")
        self.assertIn("- Working time, orchestrator turns and subagent turns joined: 0:01:00", text)
        self.assertIn("- Waiting for tools: 0:00:15", text)
        self.assertIn("- Working time without waiting for tools: 0:00:45", text)

    def test_an_exec_call_that_calls_a_subagent_tool_is_left_out_with_a_warning(self) -> None:
        rollout(self.home, "orchx", [
            meta("orchx", "10:05:00"),
            started("10:05:00", "x1"),
            context("10:05:00", "x1", "model-x"),
            {"timestamp": at("10:05:01"), "type": "response_item", "payload": {
                "type": "custom_tool_call", "name": "exec", "call_id": "c-exec",
                "input": "await tools.wait_agent({timeout_ms: 1000})"}},
            {"timestamp": at("10:05:21"), "type": "response_item", "payload": {
                "type": "custom_tool_call_output", "call_id": "c-exec", "output": "ok"}},
            tokens("10:05:30", "orchx", "x1", 10, 0, 1),
            complete("10:06:00", "x1"),
        ])
        text = self.report("orchx")
        self.assertIn("- Waiting for tools: 0:00:00", text)
        self.assertIn("- Codex session `orchx`, the orchestrator: 1 exec call(s) that call a "
                      "subagent tool: their time is left out of the waits", text)

    def test_a_call_type_the_reader_does_not_know_makes_the_wait_unknown_and_is_warned(
            self) -> None:
        rollout(self.home, "odd", [
            meta("odd", "10:02:00", "orchw", "/root/odd"),
            started("10:02:00", "d1"),
            context("10:02:00", "d1", "model-d"),
            {"timestamp": at("10:02:05"), "type": "response_item", "payload": {
                "type": "web_search_call", "status": "completed"}},
            tokens("10:02:30", "odd", "d1", 10, 0, 1),
            complete("10:03:00", "d1"),
        ])
        text = self.report("orchw")
        self.assertIn("- Waiting for tools: unknown", text)
        self.assertIn("- Codex session `orchw`, /root/odd: 1 call(s) of a type the reader does not "
                      "recognise (web_search_call): their waits are unknown", text)

    def test_a_stage_with_no_usage_reads_apart_from_one_whose_usage_was_not_read(self) -> None:
        # In `orchw` the orchestrator's usage is read, and its stretches outside the subagent turn
        # hold none: `—`. In `orchu` its rollout holds no usage at all: its stretches are `unknown`.
        stretch = "| orchestrator | 2026-10-06 10:00:00 | 0:00:00 | {} | 0 | 0 | 0 |  |"
        self.assertIn(stretch.format("—"), self.report("orchw"))
        rollout(self.home, "orchu", [
            meta("orchu", "10:00:00"),
            started("10:00:00", "u1"),
            context("10:00:00", "u1", "model-o"),
            {"timestamp": at("10:00:01"), "type": "event_msg", "payload": {
                "type": "item_completed", "thread_id": "orchu", "turn_id": "u1"}},
            complete("10:01:00", "u1"),
        ])
        rollout(self.home, "worku", [
            meta("worku", "10:00:06", "orchu", "/root/worku"),
            started("10:00:06", "w1"),
            context("10:00:06", "w1", "model-w"),
            tokens("10:00:30", "worku", "w1", 500, 200, 20),
            complete("10:00:40", "w1"),
        ])
        text = self.report("orchu")
        self.assertIn(stretch.format("unknown"), text)
        self.assertIn("| /root/worku | 2026-10-06 10:00:06 | 0:00:00 | model-w | 500 | 200 | 20 |",
                      text)

    def live(self, *last: dict) -> str:
        """The report of a session whose rollout ends with `last`, as the rollout of the session
        running this script ends while the call that runs it waits for its output."""
        rollout(self.home, "livec", [
            meta("livec", "10:00:00"),
            started("10:00:00", "l1"),
            context("10:00:00", "l1", "model-l"),
            codex_call("10:00:05", "shell", "c-one"),
            codex_call_output("10:00:20", "c-one"),
            *last,
        ])
        return self.report("livec")

    def test_a_call_the_rollout_ends_in_is_no_wait_and_no_unknown(self) -> None:
        # Codex writes the usage of the response and its item's completion after the call.
        text = self.live(codex_call("10:00:30", "shell", "c-run"),
                         tokens("10:00:30", "livec", "l1", 10, 0, 1),
                         {"timestamp": at("10:00:31"), "type": "event_msg",
                          "payload": {"type": "item_completed", "turn_id": "l1"}})
        self.assertIn("- Waiting for tools: 0:00:15", text)
        self.assertIn("Warnings: none.", text)

    def test_a_call_without_its_output_before_a_later_item_stays_unknown(self) -> None:
        for label, later in (
                ("a later output", codex_call_output("10:00:40", "c-other")),
                ("a later message", user_message("10:00:40", "go on")),
                ("the end of its turn", complete("10:00:40", "l1"))):
            with self.subTest(label):
                text = self.live(codex_call("10:00:30", "shell", "c-run"),
                                 tokens("10:00:30", "livec", "l1", 10, 0, 1), later)
                self.assertIn("- Waiting for tools: unknown", text)
                self.assertIn("1 tool call(s) with no readable result", text)


# A path written with backslashes, as a prompt on Windows names a handoff.
HANDOFF = "worktree\\.runs\\task-cycles\\t\\reports\\slice1_handoff.md"


class ClaudeFilesNamedTest(unittest.TestCase):
    """The files of `reports/` that the message starting each subagent turn names."""

    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "claude"
        project = self.home / "projects" / "C--repo"
        write_lines(project / "named.jsonl", [
            prompt("09:00:00", "run the cycle; reports/orchestrator_note.md"),
            answer("09:00:10", "o1", "opus", 1, 0, 100, 1, "end_turn"),
            prompt("09:30:00", "<task-notification>done</task-notification>"),
            answer("09:30:10", "o2", "opus", 1, 0, 100, 1, "end_turn"),
        ])
        agents = project / "named" / "subagents"
        write_lines(agents / "agent-e1.jsonl", [
            prompt("09:01:00", f"Your handoff is the file {HANDOFF}; read it."),
            answer("09:02:00", "e1", "sonnet", 1, 0, 10, 1, "tool_use"),
            # A skill loaded inside the turn names a report; it does not start the turn.
            prompt("09:02:01", "Base directory for this skill: reports/skill_example.md",
                   meta_line=True),
            answer("09:03:00", "e2", "sonnet", 1, 0, 10, 1, "end_turn"),
            prompt("09:10:00", "The coordinator sent a message: fix the findings in "
                               "`reports/review_slice1_findings.md` by the handoff "
                               ".runs/task-cycles/t/reports/slice1_fix_handoff.md; the findings "
                               "again: reports/review_slice1_findings.md", meta_line=True),
            answer("09:12:00", "e3", "sonnet", 1, 0, 10, 1, "end_turn"),
        ])
        (agents / "agent-e1.meta.json").write_text(json.dumps(
            {"agentType": "general-purpose", "description": "Executor"}), "utf-8")
        # A subagent the executor starts names a file; it is not a turn the orchestrator started.
        write_lines(agents / "agent-e2.jsonl", [
            prompt("09:02:10", "look at reports/nested_findings.md"),
            answer("09:02:20", "n1", "haiku", 1, 0, 10, 1, "end_turn"),
        ])
        (agents / "agent-e2.meta.json").write_text(json.dumps(
            {"agentType": "Explore", "description": "nested", "parentAgentId": "e1"}), "utf-8")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def session(self, name: str = "named") -> cycle_stages.Session:
        path = cycle_stages.resolve(name, Path(self.folder.name) / "codex", self.home)
        return cycle_stages.read_session(path, Path(self.folder.name) / "codex")

    def test_each_turn_holds_the_files_its_starting_message_names_once_each(self) -> None:
        rows = cycle_stages.build_rows([self.session()])
        self.assertEqual(find(rows, "Executor (general-purpose) — turn 1").named,
                         ["reports/slice1_handoff.md"])
        self.assertEqual(find(rows, "Executor (general-purpose) — turn 2").named,
                         ["reports/review_slice1_findings.md", "reports/slice1_fix_handoff.md"])

    def test_the_orchestrators_rows_name_no_file(self) -> None:
        rows = cycle_stages.build_rows([self.session()])
        self.assertEqual([[], []], [row.named for row in rows if row.name == "orchestrator"])

    def test_the_report_gives_the_files_in_a_column_of_the_stages_section(self) -> None:
        output = Path(self.folder.name) / "out" / "named.md"
        code = cycle_stages.main(["named", "--claude-home", str(self.home),
                                  "--codex-home", str(Path(self.folder.name) / "codex"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        text = output.read_text(encoding="utf-8")
        self.assertIn("| # | Stage | Start | Waiting for tools | Model | Input | Cached input "
                      "| Output | Files named |", text)
        self.assertIn("| Executor (general-purpose) — turn 2 | 2026-10-06 09:10:00 | 0:00:00 "
                      "| sonnet | 11 | 10 | 1 | reports/review_slice1_findings.md, "
                      "reports/slice1_fix_handoff.md |", text)
        self.assertIn("| orchestrator | 2026-10-06 09:00:00 | 0:00:00 | opus | 101 | 100 | 1 |  |",
                      text)

    def test_crafted_names_neither_break_a_row_nor_enter_the_column(self) -> None:
        crafted = ("reports/ok\x1b[31m.md reports/bar|x.md reports/" + "a" * 200_000 + ".md "
                   "reports/../secret.md reports/..md reports/.hidden.md reports/a..b.md "
                   "reports/-dash.md reports/x.mdx reports/y.md.bak myreports/z.md "
                   "reports/" + "b" * 117 + ".md reports/fine-name_1.md\nreports\\\\win.md "
                   "reports/tab\tname.md")
        write_lines(self.home / "projects" / "C--repo" / "named" / "subagents"
                    / "agent-e3.jsonl", [
                        prompt("09:20:00", crafted),
                        answer("09:21:00", "c1", "sonnet", 1, 0, 10, 1, "end_turn"),
                    ])
        rows = cycle_stages.build_rows([self.session()])
        [row] = [row for row in rows if row.name == "e3"]
        self.assertEqual(row.named, ["reports/" + "b" * 117 + ".md", "reports/fine-name_1.md",
                                     "reports/win.md"])
        output = Path(self.folder.name) / "out" / "crafted.md"
        self.assertEqual(0, cycle_stages.main(
            ["named", "--claude-home", str(self.home), "--codex-home",
             str(Path(self.folder.name) / "codex"), "--output", str(output)]))
        section = output.read_text(encoding="utf-8").split("\n## Stages: start", 1)[1]
        [line] = [line for line in section.splitlines() if "| e3 |" in line]
        # Nine cells: no crafted bar split one, and only the well-formed names stand in the last.
        self.assertEqual(10, line.count("|"), line)
        self.assertTrue(line.endswith(" | reports/" + "b" * 117 + ".md, reports/fine-name_1.md, "
                                      "reports/win.md |"), line)

    def test_a_name_ending_its_sentence_is_read_without_the_mark_that_ends_it(self) -> None:
        for text in ("Fix the findings in reports/review_slice4_findings.md.",
                     "Fix the findings in reports/review_slice4_findings.md, then return.",
                     "Fix the findings in `reports/review_slice4_findings.md`.",
                     "Fix the findings (reports/review_slice4_findings.md) now.",
                     "Fix the findings in [reports/review_slice4_findings.md].",
                     'Fix the findings in "reports/review_slice4_findings.md".',
                     "Fix the findings in 'reports/review_slice4_findings.md'.",
                     "Fix the findings in reports/review_slice4_findings.md...",
                     "Fix the findings in reports/review_slice4_findings.md:"):
            with self.subTest(text=text):
                self.assertEqual((["reports/review_slice4_findings.md"], False),
                                 cycle_stages.files_named(text))
        # A full stop is cut only at the end: a name that is no file of `reports/` without it
        # stays out.
        self.assertEqual(([], False), cycle_stages.files_named(
            "See reports/.md. and reports/x.md.bak. and reports/notes."))

    def test_more_files_than_the_cap_are_cut_with_a_warning(self) -> None:
        many = " ".join(f"reports/r{n:02}.md" for n in range(cycle_stages.MAX_FILES_NAMED + 5))
        write_lines(self.home / "projects" / "C--repo" / "named" / "subagents"
                    / "agent-e4.jsonl", [
                        prompt("09:20:00", many),
                        answer("09:21:00", "m1", "sonnet", 1, 0, 10, 1, "end_turn"),
                    ])
        session = self.session()
        [row] = [row for row in cycle_stages.build_rows([session]) if row.name == "e4"]
        self.assertEqual(row.named, [f"reports/r{n:02}.md"
                                     for n in range(cycle_stages.MAX_FILES_NAMED)])
        self.assertIn("Claude Code session `named`, e4: 1 turn(s) name more than "
                      f"{cycle_stages.MAX_FILES_NAMED} files of `reports/`; the rest are left "
                      "out of *Files named*", cycle_stages.find_warnings([session]))


def user_message(clock: str, text: str, turn: str | None = None) -> dict:
    payload = {"type": "message", "role": "user",
               "content": [{"type": "input_text", "text": text}]}
    if turn:
        payload["internal_chat_message_metadata_passthrough"] = {"turn_id": turn}
    return {"timestamp": at(clock), "type": "response_item", "payload": payload}


def agent_message(clock: str, recipient: str, parts: list[dict]) -> dict:
    return {"timestamp": at(clock), "type": "response_item", "payload": {
        "type": "agent_message", "author": "/root", "recipient": recipient, "content": parts}}


class CodexFilesNamedTest(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.home = Path(self.folder.name) / "codex"
        self.orchestrator = rollout(self.home, "orchn", [
            meta("orchn", "10:00:00"),
            started("10:00:00", "o1"),
            context("10:00:00", "o1", "model-o"),
            user_message("10:00:00", "run the cycle; reports/orchestrator_note.md"),
            tokens("10:00:30", "orchn", "o1", 100, 0, 10),
            complete("10:30:00", "o1"),
        ])
        rollout(self.home, "fixer", [
            meta("fixer", "10:01:00", "orchn", "/root/fixer"),
            # The forked copy of the parent's history: its message is the parent's turn's.
            meta("orchn", "10:00:00"),
            started("10:00:00", "o1"),
            user_message("10:00:00", "run the cycle; reports/orchestrator_note.md"),
            started("10:01:00", "f1"),
            context("10:01:00", "f1", "model-f"),
            agent_message("10:01:00", "/root/fixer", [
                {"type": "input_text", "text": "Message Type: NEW_TASK\nPayload:\n"},
                {"type": "input_text", "text": f"Handoff: {HANDOFF}"}]),
            tokens("10:02:00", "fixer", "f1", 1000, 0, 100),
            complete("10:03:00", "f1"),
            started("10:10:00", "f2"),
            context("10:10:00", "f2", "model-f"),
            {"timestamp": at("10:10:00"), "type": "event_msg", "payload": {
                "type": "user_message", "turn_id": "f2",
                "message": "Fix the findings in reports/review_findings.md"}},
            user_message("10:10:00", "Fix the findings in reports/review_findings.md", "f2"),
            tokens("10:11:00", "fixer", "f2", 400, 0, 40),
            complete("10:12:00", "f2"),
            started("10:20:00", "f3"),
            context("10:20:00", "f3", "model-f"),
            # An encrypted payload cannot be read: the files it names are unknown.
            agent_message("10:20:00", "/root/fixer", [
                {"type": "input_text", "text": "Message Type: FOLLOWUP\nPayload:\n"},
                {"type": "encrypted_content", "encrypted_content": "gAAAA"}]),
            tokens("10:21:00", "fixer", "f3", 50, 0, 5),
            complete("10:22:00", "f3"),
        ])

    def tearDown(self) -> None:
        self.folder.cleanup()

    def rows(self) -> list[cycle_stages.Row]:
        return cycle_stages.build_rows([cycle_stages.read_session(self.orchestrator, self.home)])

    def test_each_turn_holds_the_files_its_starting_message_names(self) -> None:
        rows = self.rows()
        self.assertEqual(find(rows, "/root/fixer — turn 1").named, ["reports/slice1_handoff.md"])
        self.assertEqual(find(rows, "/root/fixer — turn 2").named, ["reports/review_findings.md"])

    def test_a_turn_whose_message_cannot_be_read_names_unknown_files(self) -> None:
        self.assertIsNone(find(self.rows(), "/root/fixer — turn 3").named)

    def test_the_injected_instructions_before_the_prompt_are_not_the_turns_message(self) -> None:
        # Codex gives a turn the AGENTS.md text and the environment first, as user messages.
        rollout(self.home, "fresh", [
            meta("fresh", "10:40:00", "orchn", "/root/fresh"),
            started("10:40:00", "r1"),
            context("10:40:00", "r1", "model-f"),
            {"timestamp": at("10:40:00"), "type": "response_item", "payload": {
                "type": "message", "role": "user", "content": [
                    {"type": "input_text", "text": "# AGENTS.md instructions for C:\\repo\n\n"
                                                   "<INSTRUCTIONS>\nread reports/x.md\n"},
                    {"type": "input_text", "text": "<environment_context>\n  <cwd>C:\\repo</cwd>"}]}},
            user_message("10:40:01", "Fix the findings in reports/review_findings.md."),
            tokens("10:41:00", "fresh", "r1", 50, 0, 5),
            complete("10:42:00", "r1"),
        ])
        self.assertEqual(["reports/review_findings.md"], find(self.rows(), "/root/fresh").named)

    def test_the_report_writes_unknown_for_a_message_it_cannot_read(self) -> None:
        output = Path(self.folder.name) / "out" / "orchn.md"
        code = cycle_stages.main(["orchn", "--codex-home", str(self.home),
                                  "--claude-home", str(Path(self.folder.name) / "claude"),
                                  "--output", str(output)])
        self.assertEqual(code, 0)
        text = output.read_text(encoding="utf-8")
        self.assertIn("| /root/fixer — turn 3 | 2026-10-06 10:20:00 | 0:00:00 | model-f | 50 | 0 "
                      "| 5 | unknown |", text)
        self.assertIn("| /root/fixer — turn 2 | 2026-10-06 10:10:00 | 0:00:00 | model-f | 400 | 0 "
                      "| 40 | reports/review_findings.md |", text)


class CommandTest(unittest.TestCase):
    def test_an_unknown_session_fails_with_a_message(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                code = cycle_stages.main(["nope", "--codex-home", folder, "--claude-home", folder])
        self.assertEqual(code, 1)
        self.assertIn("Error: no transcript of session 'nope'", stderr.getvalue())

    def current(self, **variables: str) -> str:
        saved = {name: os.environ.pop(name, None) for name in cycle_stages.SESSION_VARIABLES}
        try:
            os.environ.update(variables)
            return cycle_stages.current_session()
        finally:
            for name, value in saved.items():
                os.environ.pop(name, None)
                if value is not None:
                    os.environ[name] = value

    def test_without_a_session_the_running_one_is_taken(self) -> None:
        self.assertEqual(self.current(CODEX_SESSION_ID="codex-id"), "codex-id")
        self.assertEqual(self.current(CLAUDE_CODE_SESSION_ID="claude-id"), "claude-id")

    def test_without_a_session_and_without_a_variable_it_fails(self) -> None:
        with self.assertRaisesRegex(cycle_stages.CycleStagesError, "name a session; neither"):
            self.current()

    def test_without_a_session_and_with_both_variables_it_fails(self) -> None:
        with self.assertRaisesRegex(cycle_stages.CycleStagesError, "name a session; both"):
            self.current(CODEX_SESSION_ID="codex-id", CLAUDE_CODE_SESSION_ID="claude-id")


if __name__ == "__main__":
    unittest.main()
