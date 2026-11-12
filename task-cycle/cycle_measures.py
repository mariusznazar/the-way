"""The measures of how the agents of one run of the task cycle use the context and the prompt cache
of the model, counted from the session transcripts that Claude Code keeps.

Usage:

    python -B task-cycle/cycle_measures.py [SESSION ...] [--output PATH]
        [--codex-home DIR] [--claude-home DIR]

SESSION names one session of the cycle's orchestrator: the path of its transcript, or its id, found
as `<claude home>/projects/*/<id>.jsonl`. The homes default to the environment variables CODEX_HOME
and CLAUDE_CONFIG_DIR, and otherwise to `~/.codex` and `~/.claude`. Name every session of the run, in
any order. Without SESSION, the session is taken from CLAUDE_CODE_SESSION_ID or CODEX_SESSION_ID,
the one of the two that is set; where both or neither is set, SESSION has to be named.

The subagents of a session are `<transcript without .jsonl>/subagents/agent-<id>.jsonl`, each
described by `agent-<id>.meta.json` beside it. Each one is an agent of its own.

A call is one model response of an agent. Claude Code writes a response over several lines that
share its id; each id counts once, from the line with the most output tokens. A response whose model
is `<synthetic>` is no call.

The file is Markdown, written to PATH or printed. Exit code: 0 when it is written; 2 with
`Error: <message>` on stderr and nothing written otherwise, for a session that cannot be found or
read, a line that is not JSON and a needed field that is missing.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


class MeasuresError(Exception):
    """A session that cannot be found or read, or a transcript that lacks a field it needs."""


SESSION_VARIABLES = ("CLAUDE_CODE_SESSION_ID", "CODEX_SESSION_ID")
TOOL = "Claude Code"
SYNTHETIC_MODEL = "<synthetic>"
REWRITE_FLOOR = 2000
REWRITE_SHRINK_LIMIT = (7, 10)  # a context that falls to 7/10 of the previous one or less is a collapse
LARGE_CONTEXT = 200000
EARLIEST = datetime.min.replace(tzinfo=timezone.utc)


@dataclass(frozen=True)
class Call:
    at: datetime
    index: int
    input: int
    read: int
    write: int
    write_5m: int
    write_1h: int

    @property
    def context(self) -> int:
        return self.input + self.read + self.write


@dataclass
class Agent:
    name: str
    orchestrator: bool
    calls: list[Call]


def parse_time(value: object) -> datetime:
    """The time of a transcript line, in UTC; a line with no readable time sorts first."""
    if not isinstance(value, str):
        return EARLIEST
    try:
        at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return EARLIEST
    return at if at.tzinfo else at.replace(tzinfo=timezone.utc)


def member(holder: object, key: str, name: str, where: str) -> object:
    value = holder.get(key) if isinstance(holder, dict) else None
    if value is None:
        raise MeasuresError(f"{where}: no field {name}")
    return value


def whole(holder: object, key: str, name: str, where: str) -> int:
    value = member(holder, key, name, where)
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise MeasuresError(f"{where}: field {name} is not a whole number")
    return value


def read_response(entry: dict, where: str, index: int) -> tuple[str, int, Call]:
    """The identifier of a response, its output tokens and its call, from its line. Every needed
    field is read: a missing one ends the reading, it is never taken as zero."""
    message = member(entry, "message", "message", where)
    usage = member(message, "usage", "message.usage", where)
    five_and_one = member(usage, "cache_creation", "message.usage.cache_creation", where)
    write = whole(usage, "cache_creation_input_tokens", "message.usage.cache_creation_input_tokens",
                  where)
    call = Call(
        at=parse_time(entry.get("timestamp")),
        index=index,
        input=whole(usage, "input_tokens", "message.usage.input_tokens", where),
        read=whole(usage, "cache_read_input_tokens", "message.usage.cache_read_input_tokens", where),
        write=write,
        write_5m=whole(five_and_one, "ephemeral_5m_input_tokens",
                       "message.usage.cache_creation.ephemeral_5m_input_tokens", where),
        write_1h=whole(five_and_one, "ephemeral_1h_input_tokens",
                       "message.usage.cache_creation.ephemeral_1h_input_tokens", where),
    )
    output = whole(usage, "output_tokens", "message.usage.output_tokens", where)
    ident = message.get("id")
    if not isinstance(ident, str) or not ident:
        ident = f"line {index}"
    return ident, output, call


def read_calls(path: Path) -> list[Call]:
    """The calls of the agent whose transcript this is, in the order of their time."""
    chosen: dict[str, tuple[int, Call]] = {}
    first = True
    try:
        with path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                where = f"{path}:{number}"
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as error:
                    raise MeasuresError(f"{where}: not JSON: {error}") from error
                if not isinstance(entry, dict):
                    raise MeasuresError(f"{where}: not a JSON object")
                if first and entry.get("type") == "session_meta":
                    raise MeasuresError(f"{path} is a Codex rollout; the measures count Claude "
                                        "Code transcripts")
                first = False
                if entry.get("type") != "assistant":
                    continue
                message = entry.get("message")
                if isinstance(message, dict) and message.get("model") == SYNTHETIC_MODEL:
                    continue
                ident, output, call = read_response(entry, where, number)
                kept = chosen.get(ident)
                if kept is None or output >= kept[0]:
                    chosen[ident] = (output, call)
    except (OSError, UnicodeDecodeError) as error:
        raise MeasuresError(f"cannot read {path}: {error}") from error
    calls = [call for _, call in chosen.values()]
    calls.sort(key=lambda call: (call.at, call.index))
    return calls


def cell(text: str) -> str:
    """Text from a transcript on one line, with each bar and control character replaced, so that
    it cannot break the table."""
    cleaned = "".join(" " if unicodedata.category(char).startswith("C") else char for char in text)
    return " ".join(cleaned.split()).replace("|", "/")


def read_subagent_name(transcript: Path, agent_id: str) -> str:
    """`<description> (<agentType>)` from the agent's meta file; the id where the file or the
    keys are missing."""
    meta_path = transcript.with_name(f"{transcript.stem}.meta.json")
    meta: object = {}
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise MeasuresError(f"cannot read {meta_path}: {error}") from error
    if not isinstance(meta, dict):
        meta = {}
    description = meta.get("description") or agent_id
    kind = meta.get("agentType")
    return f"{description} ({kind})" if kind else str(description)


def read_session(path: Path) -> list[Agent]:
    """The orchestrator of a session and each subagent of its folder, each as an agent."""
    session_id = path.stem
    agents = [Agent(f"orchestrator {session_id}", True, read_calls(path))]
    folder = path.with_suffix("") / "subagents"
    if folder.is_dir():
        for transcript in sorted(folder.glob("agent-*.jsonl")):
            agent_id = transcript.stem.removeprefix("agent-")
            agents.append(Agent(read_subagent_name(transcript, agent_id), False,
                                read_calls(transcript)))
    return agents


# The measures


def rewrites(calls: list[Call]) -> list[int]:
    """The tokens written again in each call of an agent that counts as a rewrite. What the earlier
    call held in the cache and the later one did not read, at most what the later one wrote; it
    counts only above the floor, and not where the context fell by 30% or more."""
    counted = []
    for before, after in zip(calls, calls[1:]):
        held = before.read + before.write
        amount = min(max(0, held - after.read), after.write)
        shrink_numerator, shrink_denominator = REWRITE_SHRINK_LIMIT
        collapsed = after.context * shrink_denominator <= before.context * shrink_numerator
        if amount > REWRITE_FLOOR and not collapsed:
            counted.append(amount)
    return counted


def mean(total: int, count: int) -> str:
    if count == 0:
        return "unknown"
    return str((2 * total + count) // (2 * count))


def share(part: int, whole_total: int) -> str:
    """The share in per cent to one decimal, half up."""
    if whole_total == 0:
        return "unknown"
    tenths = (2000 * part + whole_total) // (2 * whole_total)
    return f"{tenths // 10}.{tenths % 10}%"


def position(calls: list[Call], which: str) -> str:
    if not calls:
        return "unknown"
    index = {"first": 0, "middle": (len(calls) - 1) // 2, "last": len(calls) - 1}[which]
    return str(calls[index].context)


def agent_row(agent: Agent) -> str:
    counted = rewrites(agent.calls)
    values = [
        cell(agent.name),
        TOOL,
        str(len(agent.calls)),
        position(agent.calls, "first"),
        position(agent.calls, "middle"),
        position(agent.calls, "last"),
        str(sum(call.write_5m for call in agent.calls)),
        str(sum(call.write_1h for call in agent.calls)),
        str(sum(counted)),
        str(len(counted)),
    ]
    return "| " + " | ".join(values) + " |"


def report(agents: list[Agent]) -> str:
    orchestrators = [agent for agent in agents if agent.orchestrator]
    subagents = [agent for agent in agents if not agent.orchestrator]
    # The sessions are in the order they were read in, so the stable sort keeps a tie in that order.
    orchestrator_calls = sorted((call for agent in orchestrators for call in agent.calls),
                                key=lambda call: call.at)
    subagent_calls = [call for agent in subagents for call in agent.calls]
    everything = orchestrator_calls + subagent_calls
    contexts = [call.context for call in everything]
    total_context = sum(contexts)
    large_context = sum(context for context in contexts if context > LARGE_CONTEXT)
    orchestrator_counted = [amount for agent in orchestrators for amount in rewrites(agent.calls)]
    subagent_counted = [amount for agent in subagents for amount in rewrites(agent.calls)]
    orchestrator_context = sum(call.context for call in orchestrator_calls)
    rows = [agent_row(agent) for agent in agents]

    lines = [
        "# Measures of the cycle run",
        "",
        f"- Calls in all: {len(everything)}",
        f"- Calls of the orchestrator: {len(orchestrator_calls)}",
        f"- Calls of subagents: {len(subagent_calls)}",
        f"- Mean context per call: {mean(total_context, len(everything))}",
        f"- Mean context per call of the orchestrator: "
        f"{mean(orchestrator_context, len(orchestrator_calls))}",
        f"- Share of the context in calls above 200000 tokens: {share(large_context, total_context)}",
        f"- Context of the orchestrator's first call: {position(orchestrator_calls, 'first')}",
        f"- Context of the orchestrator's middle call: {position(orchestrator_calls, 'middle')}",
        f"- Context of the orchestrator's last call: {position(orchestrator_calls, 'last')}",
        f"- Cache written, 5 minutes: {sum(call.write_5m for call in everything)}",
        f"- Cache written, 1 hour: {sum(call.write_1h for call in everything)}",
        f"- Cache written again by the orchestrator: {sum(orchestrator_counted)}",
        f"- Calls of the orchestrator with a cache write again: {len(orchestrator_counted)}",
        f"- Cache written again by subagents: {sum(subagent_counted)}",
        f"- Calls of subagents with a cache write again: {len(subagent_counted)}",
        "",
        "## Agents",
        "",
        "| Agent | Tool | Calls | First call | Middle call | Last call | Cache written, 5 minutes "
        "| Cache written, 1 hour | Cache written again | Calls with a cache write again |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        *rows,
    ]
    return "\n".join(lines) + "\n"


# Finding sessions


def default_home(variable: str, folder: str) -> Path:
    value = os.environ.get(variable)
    return Path(value) if value else Path.home() / folder


def current_session() -> str:
    """The id of the session running this command, from the variable its tool sets."""
    found = {name: os.environ[name] for name in SESSION_VARIABLES if os.environ.get(name)}
    if len(found) == 1:
        return next(iter(found.values()))
    if not found:
        raise MeasuresError("name a session; neither " + " nor ".join(SESSION_VARIABLES)
                            + " is set")
    raise MeasuresError("name a session; both " + " and ".join(SESSION_VARIABLES) + " are set")


def resolve(name: str, codex_home: Path, claude_home: Path) -> Path:
    path = Path(name)
    if path.is_file():
        return path
    found = sorted((claude_home / "projects").glob(f"*/{name}.jsonl"))
    found += sorted((codex_home / "sessions").glob(f"**/rollout-*-{name}.jsonl"))
    if len(found) == 1:
        return found[0]
    if not found:
        raise MeasuresError(f"no transcript of session {name!r}")
    raise MeasuresError(f"session {name!r} matches several transcripts: "
                        + ", ".join(str(path) for path in found))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("sessions", nargs="*", metavar="SESSION")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--codex-home", type=Path, default=default_home("CODEX_HOME", ".codex"))
    parser.add_argument("--claude-home", type=Path,
                        default=default_home("CLAUDE_CONFIG_DIR", ".claude"))
    args = parser.parse_args(argv)
    try:
        names = args.sessions or [current_session()]
        paths = dict.fromkeys(resolve(name, args.codex_home, args.claude_home).resolve()
                              for name in names)
        agents: list[Agent] = []
        for path in sorted(paths, key=lambda path: path.stem):
            agents.extend(read_session(path))
        text = report(agents)
    except MeasuresError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
    data = text.encode("utf-8")
    try:
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_bytes(data)
        else:
            sys.stdout.buffer.write(data)
    except OSError as error:
        print(f"Error: cannot write the measures: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
