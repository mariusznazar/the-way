"""The measures of how the agents of one run of the task cycle use the context and the prompt cache
of the model, counted from the session transcripts that Claude Code keeps and the rollouts that
Codex keeps.

Usage:

    python -B task-cycle/cycle_measures.py [SESSION ...] [--output PATH]
        [--codex-home DIR] [--claude-home DIR]

SESSION names one session of the cycle's orchestrator: the path of its transcript or rollout, or its
id, found as `<claude home>/projects/*/<id>.jsonl` or `<codex home>/sessions/**/rollout-*-<id>.jsonl`.
The homes default to the environment variables CODEX_HOME and CLAUDE_CONFIG_DIR, and otherwise to
`~/.codex` and `~/.claude`. Name every session of the run, in any order; sessions of both tools may be
named together. Without SESSION, the session is taken from CLAUDE_CODE_SESSION_ID or CODEX_SESSION_ID,
the one of the two that is set; where both or neither is set, SESSION has to be named.

The subagents of a Claude Code session are `<transcript without .jsonl>/subagents/agent-<id>.jsonl`,
each described by `agent-<id>.meta.json` beside it. The subagents of a Codex session are the rollouts
under `<codex home>/sessions` whose session_meta names the orchestrator's id, or the id of a subagent
already found, as its parent_thread_id. Each one is an agent of its own.

A call of a Claude Code agent is one model response. Claude Code writes a response over several lines
that share its id; each id counts once, from the line with the most output tokens. A response whose
model is `<synthetic>` is no call.

A call of a Codex agent is one token usage record of the agent's own thread. Its context is its
input tokens, which already hold the part read from the cache. Codex's record gives no cache write,
so the cache figures of a Codex agent are unknown, never zero.

The file is Markdown, written to PATH or printed. Exit code: 0 when it is written; 2 with
`Error: <message>` on stderr and nothing written otherwise, for a session that cannot be found or
read, a line that is not JSON, a needed field that is missing or no whole number, and a rollout of a
subagent named as a session.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


class MeasuresError(Exception):
    """A session that cannot be found or read, or a transcript that lacks a field it needs."""


SESSION_VARIABLES = ("CLAUDE_CODE_SESSION_ID", "CODEX_SESSION_ID")
CLAUDE = "Claude Code"
CODEX = "Codex"
UNKNOWN = "unknown"
SYNTHETIC_MODEL = "<synthetic>"
REWRITE_FLOOR = 2000
REWRITE_SHRINK_LIMIT = (7, 10)  # a context that falls to 7/10 of the previous one or less is a collapse
LARGE_CONTEXT = 200000


@dataclass(frozen=True)
class Call:
    at: datetime
    index: int
    context: int
    read: int | None  # None where the record gives no cache read: a Codex call
    write: int | None
    write_5m: int | None
    write_1h: int | None


@dataclass
class Agent:
    name: str
    orchestrator: bool
    calls: list[Call]
    tool: str = CLAUDE

    @property
    def cache_known(self) -> bool:
        return self.tool != CODEX


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


def identifier(holder: object, key: str, name: str, where: str) -> str:
    value = member(holder, key, name, where)
    if not isinstance(value, str) or not value:
        raise MeasuresError(f"{where}: field {name} is not an identifier")
    return value


def read_time(entry: dict, where: str) -> datetime:
    """The time of a line, in UTC. A missing or unreadable time ends the reading."""
    value = member(entry, "timestamp", "timestamp", where)
    if not isinstance(value, str):
        raise MeasuresError(f"{where}: field timestamp is not a time")
    try:
        at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise MeasuresError(f"{where}: field timestamp is not a time") from error
    return at if at.tzinfo else at.replace(tzinfo=timezone.utc)


def json_lines(path: Path) -> Iterator[tuple[int, dict]]:
    """Each non-blank line of a JSON Lines file, as its number and its object. A line that is not
    JSON, or not an object, ends the reading with the file and the line named."""
    try:
        with path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if not line.strip():
                    continue
                where = f"{path}:{number}"
                try:
                    entry = json.loads(line)
                except (ValueError, RecursionError) as error:
                    raise MeasuresError(f"{where}: not JSON: {error}") from error
                if not isinstance(entry, dict):
                    raise MeasuresError(f"{where}: not a JSON object")
                yield number, entry
    except (OSError, UnicodeDecodeError) as error:
        raise MeasuresError(f"cannot read {path}: {error}") from error


def read_response(entry: dict, where: str, index: int) -> tuple[str, int, Call]:
    """The identifier of a response, its output tokens and its call, from its line. Every needed
    field is read: a missing one ends the reading, it is never taken as zero."""
    message = member(entry, "message", "message", where)
    usage = member(message, "usage", "message.usage", where)
    five_and_one = member(usage, "cache_creation", "message.usage.cache_creation", where)
    write = whole(usage, "cache_creation_input_tokens", "message.usage.cache_creation_input_tokens",
                  where)
    input_tokens = whole(usage, "input_tokens", "message.usage.input_tokens", where)
    read = whole(usage, "cache_read_input_tokens", "message.usage.cache_read_input_tokens", where)
    write_5m = whole(five_and_one, "ephemeral_5m_input_tokens",
                     "message.usage.cache_creation.ephemeral_5m_input_tokens", where)
    write_1h = whole(five_and_one, "ephemeral_1h_input_tokens",
                     "message.usage.cache_creation.ephemeral_1h_input_tokens", where)
    call = Call(
        at=read_time(entry, where),
        index=index,
        context=input_tokens + read + write,
        read=read,
        write=write,
        write_5m=write_5m,
        write_1h=write_1h,
    )
    output = whole(usage, "output_tokens", "message.usage.output_tokens", where)
    ident = identifier(message, "id", "message.id", where)
    return ident, output, call


def read_calls(path: Path) -> list[Call]:
    """The calls of the Claude Code agent whose transcript this is, in the order of their time."""
    chosen: dict[str, tuple[int, Call]] = {}
    for number, entry in json_lines(path):
        if entry.get("type") != "assistant":
            continue
        message = entry.get("message")
        if isinstance(message, dict) and message.get("model") == SYNTHETIC_MODEL:
            continue
        ident, output, call = read_response(entry, f"{path}:{number}", number)
        kept = chosen.get(ident)
        if kept is None or output >= kept[0]:
            chosen[ident] = (output, call)
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
        except (OSError, UnicodeDecodeError, ValueError, RecursionError) as error:
            raise MeasuresError(f"cannot read {meta_path}: {error}") from error
    if not isinstance(meta, dict):
        meta = {}
    description = meta.get("description") or agent_id
    kind = meta.get("agentType")
    return f"{description} ({kind})" if kind else str(description)


def read_claude_session(path: Path) -> list[Agent]:
    """The orchestrator of a Claude Code session and each subagent of its folder, each as an agent."""
    session_id = path.stem
    agents = [Agent(f"orchestrator {session_id}", True, read_calls(path))]
    folder = path.with_suffix("") / "subagents"
    if folder.is_dir():
        for transcript in sorted(folder.glob("agent-*.jsonl")):
            agent_id = transcript.stem.removeprefix("agent-")
            agents.append(Agent(read_subagent_name(transcript, agent_id), False,
                                read_calls(transcript)))
    return agents


# Codex

@dataclass(frozen=True)
class RolloutMeta:
    ident: str
    parent: str | None
    name: str  # the agent's path, else its nickname, else its id


def rollout_meta(path: Path) -> RolloutMeta | None:
    """The identity of a rollout, read from its first line; None where that line is not the
    session_meta of a Codex rollout."""
    first = next(json_lines(path), None)
    if first is None:
        return None
    number, entry = first
    if entry.get("type") != "session_meta":
        return None
    where = f"{path}:{number}"
    payload = member(entry, "payload", "payload", where)
    if not isinstance(payload, dict):
        raise MeasuresError(f"{where}: field payload is not an object")
    ident = identifier(payload, "id", "payload.id", where)
    parent = payload.get("parent_thread_id") or None
    if parent is not None and not isinstance(parent, str):
        raise MeasuresError(f"{where}: field payload.parent_thread_id is not an identifier")
    name = ident
    for key in ("agent_path", "agent_nickname"):
        value = payload.get(key)
        if isinstance(value, str) and value:
            name = value
            break
    return RolloutMeta(ident, parent, name)


def read_codex_calls(path: Path, ident: str) -> list[Call]:
    """The calls of the agent whose thread is `ident`: the token usage records of that thread, in
    the order of their time. A forked subagent's rollout repeats its parent's records, which are no
    calls of its own."""
    calls = []
    for number, entry in json_lines(path):
        if entry.get("type") != "token_usage_record":
            continue
        where = f"{path}:{number}"
        payload = member(entry, "payload", "payload", where)
        if identifier(payload, "thread_id", "payload.thread_id", where) != ident:
            continue
        usage = member(payload, "usage", "payload.usage", where)
        input_tokens = whole(usage, "input_tokens", "payload.usage.input_tokens", where)
        calls.append(Call(at=read_time(entry, where), index=number, context=input_tokens,
                          read=None, write=None, write_5m=None, write_1h=None))
    calls.sort(key=lambda call: (call.at, call.index))
    return calls


def codex_subagents(home: Path, root: str) -> list[tuple[Path, RolloutMeta]]:
    """Every rollout under `home/sessions` that descends from `root`, as its path and identity. A
    rollout descends from a rollout whose id its parent_thread_id names; the search goes level by
    level, each level in the order of the paths."""
    children: dict[str, list[tuple[Path, RolloutMeta]]] = {}
    sessions = home / "sessions"
    if sessions.is_dir():
        for path in sorted(sessions.rglob("rollout-*.jsonl")):
            meta = rollout_meta(path)
            if meta is not None and meta.parent is not None:
                children.setdefault(meta.parent, []).append((path, meta))
    found: list[tuple[Path, RolloutMeta]] = []
    known = {root}
    queue = [root]
    while queue:
        for path, meta in children.get(queue.pop(0), []):
            if meta.ident not in known:
                known.add(meta.ident)
                found.append((path, meta))
                queue.append(meta.ident)
    return found


def read_codex_session(path: Path, meta: RolloutMeta, codex_home: Path) -> list[Agent]:
    """The orchestrator of a Codex session and each subagent under it, each as an agent."""
    if meta.parent is not None:
        raise MeasuresError(f"{path} is a subagent's rollout, not an orchestrator's")
    agents = [Agent(f"orchestrator {meta.ident}", True, read_codex_calls(path, meta.ident), CODEX)]
    for sub_path, sub in codex_subagents(codex_home, meta.ident):
        agents.append(Agent(sub.name, False, read_codex_calls(sub_path, sub.ident), CODEX))
    return agents


def read_session(path: Path, codex_home: Path) -> list[Agent]:
    """The agents of one session, of either tool."""
    meta = rollout_meta(path)
    if meta is None:
        return read_claude_session(path)
    return read_codex_session(path, meta, codex_home)


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


def cache_sum(agents: list[Agent], field: str) -> str:
    """The sum of a cache figure over the agents, unknown where one of them is a Codex agent, whose
    record gives no cache write."""
    if not all(agent.cache_known for agent in agents):
        return UNKNOWN
    return str(sum(getattr(call, field) for agent in agents for call in agent.calls))


def rewrite_totals(agents: list[Agent]) -> tuple[str, str]:
    """The tokens written again and the calls with a cache write again, summed over the agents;
    unknown where one of them is a Codex agent."""
    if not all(agent.cache_known for agent in agents):
        return UNKNOWN, UNKNOWN
    counted = [amount for agent in agents for amount in rewrites(agent.calls)]
    return str(sum(counted)), str(len(counted))


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
    written_again, calls_again = rewrite_totals([agent])
    values = [
        cell(agent.name),
        agent.tool,
        str(len(agent.calls)),
        position(agent.calls, "first"),
        position(agent.calls, "middle"),
        position(agent.calls, "last"),
        cache_sum([agent], "write_5m"),
        cache_sum([agent], "write_1h"),
        written_again,
        calls_again,
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
    orchestrator_context = sum(call.context for call in orchestrator_calls)
    orchestrator_again, orchestrator_again_calls = rewrite_totals(orchestrators)
    subagent_again, subagent_again_calls = rewrite_totals(subagents)
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
        f"- Cache written, 5 minutes: {cache_sum(agents, 'write_5m')}",
        f"- Cache written, 1 hour: {cache_sum(agents, 'write_1h')}",
        f"- Cache written again by the orchestrator: {orchestrator_again}",
        f"- Calls of the orchestrator with a cache write again: {orchestrator_again_calls}",
        f"- Cache written again by subagents: {subagent_again}",
        f"- Calls of subagents with a cache write again: {subagent_again_calls}",
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
            agents.extend(read_session(path, args.codex_home))
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
