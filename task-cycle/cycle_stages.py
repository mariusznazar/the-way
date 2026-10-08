"""The stages of one run of the task cycle — how long each took, which models did it and how many
tokens it used — counted from the session transcripts that Codex and Claude Code keep.

Usage:

    python -B task-cycle/cycle_stages.py [SESSION ...] [--output PATH]
        [--codex-home DIR] [--claude-home DIR]

SESSION names one session of the cycle's orchestrator: the path of its transcript, or its id. A
Codex id is looked up as `<codex home>/sessions/**/rollout-*-<id>.jsonl`, a Claude Code id as
`<claude home>/projects/*/<id>.jsonl`. The homes default to the environment variables CODEX_HOME
and CLAUDE_CONFIG_DIR, and otherwise to `~/.codex` and `~/.claude`. Name every session of the run,
in any order; without SESSION, the Claude Code session named by CLAUDE_CODE_SESSION_ID is taken.

The subagents of a session are found where each tool keeps them. A Codex subagent is a rollout of
its own whose first line, `session_meta`, names the orchestrator's id as `parent_thread_id`; a
Claude Code subagent is `<transcript without .jsonl>/subagents/agent-<id>.jsonl`, described by
`agent-<id>.meta.json` beside it. A subagent started by another subagent counts towards the stage
of the subagent the orchestrator started.

A stage is either one turn of a subagent the orchestrator started — from the prompt that sets it
working, when it starts or in a later follow-up, to its answer — or a stretch in which the
orchestrator works while no such turn runs. A subagent turn lasts from its first to its last entry;
a stretch of the orchestrator counts only the time inside the orchestrator's own turns, so waiting
for the human is left out. A token count belongs to the stage running when its entry is written:
the subagent's to the turn it falls in, the orchestrator's to the subagent turn then running or to
the orchestrator's stretch; while several subagent turns run at once, the orchestrator's tokens go
to a row of their own naming them, rather than being split by a guess.

Tokens are counted as each tool reports them per model response: input with the part read from a
cache, and output with reasoning. Claude Code writes one response over several lines that repeat
its usage; each response counts once.

The report is Markdown, written to PATH or printed. Exit code: 0 on success; 1 with
`Error: <message>` on stderr otherwise.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path


class CycleStagesError(Exception):
    """A session that cannot be found or read."""


@dataclass
class Usage:
    input: int = 0
    cached: int = 0
    output: int = 0

    def add(self, other: Usage) -> None:
        self.input += other.input
        self.cached += other.cached
        self.output += other.output

    @property
    def total(self) -> int:
        return self.input + self.output


@dataclass
class Record:
    at: datetime
    usage: Usage
    model: str | None


@dataclass
class Agent:
    key: str
    name: str
    parent: str | None
    turns: list[tuple[datetime, datetime]] = field(default_factory=list)
    records: list[Record] = field(default_factory=list)


@dataclass
class Session:
    tool: str
    id: str
    path: Path
    orchestrator: Agent
    subagents: list[Agent]


@dataclass
class Row:
    start: datetime
    name: str
    duration: timedelta | None
    subagent: Usage = field(default_factory=Usage)
    orchestrator: Usage = field(default_factory=Usage)
    subagent_models: list[str] = field(default_factory=list)
    orchestrator_models: list[str] = field(default_factory=list)
    window: tuple[datetime, datetime] | None = None


def parse_time(text: str) -> datetime:
    return datetime.fromisoformat(text.replace("Z", "+00:00"))


def read_lines(path: Path):
    try:
        with path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if line.strip():
                    try:
                        yield json.loads(line)
                    except json.JSONDecodeError as error:
                        raise CycleStagesError(f"{path}:{number}: not JSON: {error}") from error
    except OSError as error:
        raise CycleStagesError(f"cannot read {path}: {error}") from error


def first_line(path: Path) -> dict:
    for entry in read_lines(path):
        return entry
    raise CycleStagesError(f"{path} is empty")


# Codex


def codex_meta(path: Path) -> dict | None:
    entry = first_line(path)
    if entry.get("type") != "session_meta":
        return None
    return entry.get("payload") or {}


def read_codex_agent(path: Path, parent: str | None) -> Agent:
    meta = codex_meta(path)
    if meta is None:
        raise CycleStagesError(f"{path} does not start with a Codex session_meta line")
    own = meta["id"]
    name = meta.get("agent_path") or meta.get("agent_nickname") or own
    starts: dict[str, datetime] = {}
    ends: dict[str, datetime] = {}
    first_seen: dict[str, datetime] = {}
    last_seen: dict[str, datetime] = {}
    models: dict[str, str] = {}
    own_turns: set[str] = set()
    raw: list[tuple[datetime, str, dict]] = []
    for entry in read_lines(path):
        payload = entry.get("payload")
        if not isinstance(payload, dict) or "timestamp" not in entry:
            continue
        at = parse_time(entry["timestamp"])
        kind = entry.get("type")
        turn = payload.get("turn_id")
        if turn:
            first_seen.setdefault(turn, at)
            last_seen[turn] = at
        if kind == "event_msg":
            event = payload.get("type")
            if event == "task_started":
                starts.setdefault(turn, at)
            elif event == "task_complete":
                ends[turn] = at
            elif event == "item_completed" and payload.get("thread_id") == own:
                own_turns.add(turn)
        elif kind == "turn_context" and turn:
            models[turn] = payload.get("model")
        elif kind == "token_usage_record" and payload.get("thread_id") == own:
            own_turns.add(turn)
            raw.append((at, turn, payload.get("usage") or {}))
    # A forked subagent's rollout repeats its parent's history; only turns that the subagent's
    # own thread worked in are its turns.
    agent = Agent(own, name, parent)
    for turn in own_turns:
        start = starts.get(turn) or first_seen[turn]
        agent.turns.append((start, ends.get(turn) or last_seen[turn]))
    agent.turns.sort()
    for at, turn, usage in raw:
        agent.records.append(Record(at, Usage(
            usage.get("input_tokens", 0),
            usage.get("cached_input_tokens", 0),
            usage.get("output_tokens", 0),
        ), models.get(turn)))
    return agent


def codex_subagent_paths(home: Path, root: str, since: datetime) -> list[tuple[Path, str]]:
    """Every rollout under `home/sessions` descending from `root`, with its parent's id."""
    parents: dict[str, tuple[Path, str]] = {}
    floor = since.timestamp() - 1
    for path in (home / "sessions").rglob("rollout-*.jsonl"):
        if path.stat().st_mtime < floor:
            continue
        meta = codex_meta(path)
        if meta and meta.get("parent_thread_id"):
            parents[meta["id"]] = (path, meta["parent_thread_id"])
    found: dict[str, tuple[Path, str]] = {}
    known = {root}
    while True:
        new = {i: v for i, v in parents.items() if v[1] in known and i not in found}
        if not new:
            break
        found.update(new)
        known.update(new)
    return sorted(found.values())


def read_codex_session(path: Path, codex_home: Path) -> Session:
    orchestrator = read_codex_agent(path, None)
    orchestrator.name = "orchestrator"
    since = min((start for start, _ in orchestrator.turns), default=datetime.fromtimestamp(0))
    subagents = [read_codex_agent(p, parent) for p, parent in
                 codex_subagent_paths(codex_home, orchestrator.key, since)]
    return Session("Codex", orchestrator.key, path, orchestrator, subagents)


# Claude Code


def is_text(entry: dict) -> bool:
    """A user line holding text rather than a tool's result."""
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    return bool(content) and isinstance(content[0], dict) and content[0].get("type") == "text"


def read_claude_agent(path: Path, key: str, name: str, parent: str | None) -> Agent:
    responses: dict[str, tuple[datetime, dict, str | None]] = {}
    prompts: list[datetime] = []
    activity: list[datetime] = []
    answered = True
    for entry in read_lines(path):
        if "timestamp" not in entry:
            continue
        at = parse_time(entry["timestamp"])
        if entry.get("type") == "user":
            # Text the human types, or a notice, sets the agent working; text the tool adds
            # (a loaded skill, a message from the coordinator) does so only once the agent has
            # answered, and is part of the running turn otherwise.
            if is_text(entry) and (not entry.get("isMeta") or answered):
                prompts.append(at)
                answered = False
            else:
                activity.append(at)
        elif entry.get("type") == "assistant":
            message = entry.get("message") or {}
            model = message.get("model")
            if model == "<synthetic>":
                continue
            activity.append(at)
            if message.get("stop_reason"):
                answered = message["stop_reason"] == "end_turn"
            usage = message.get("usage") or {}
            ident = message.get("id") or entry.get("uuid")
            kept = responses.get(ident)
            if kept is None or usage.get("output_tokens", 0) >= kept[1].get("output_tokens", 0):
                responses[ident] = (at, usage, model)
    agent = Agent(key, name, parent)
    prompts.sort()
    activity.sort()
    for index, start in enumerate(prompts):
        stop = prompts[index + 1] if index + 1 < len(prompts) else None
        inside = [at for at in activity if at >= start and (stop is None or at < stop)]
        if inside:
            agent.turns.append((start, inside[-1]))
    for at, usage, model in responses.values():
        agent.records.append(Record(at, Usage(
            usage.get("input_tokens", 0) + usage.get("cache_creation_input_tokens", 0)
            + usage.get("cache_read_input_tokens", 0),
            usage.get("cache_read_input_tokens", 0),
            usage.get("output_tokens", 0),
        ), model))
    agent.records.sort(key=lambda record: record.at)
    return agent


def read_claude_session(path: Path) -> Session:
    session_id = path.stem
    orchestrator = read_claude_agent(path, session_id, "orchestrator", None)
    subagents: list[Agent] = []
    folder = path.with_suffix("") / "subagents"
    if folder.is_dir():
        for transcript in sorted(folder.glob("agent-*.jsonl")):
            agent_id = transcript.stem.removeprefix("agent-")
            meta_path = transcript.with_name(f"{transcript.stem}.meta.json")
            meta: dict = {}
            if meta_path.is_file():
                try:
                    meta = json.loads(meta_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as error:
                    raise CycleStagesError(f"cannot read {meta_path}: {error}") from error
            description = meta.get("description") or agent_id
            kind = meta.get("agentType")
            name = f"{description} ({kind})" if kind else description
            subagents.append(read_claude_agent(
                transcript, agent_id, name, meta.get("parentAgentId") or session_id))
    known = {agent.key for agent in subagents}
    for agent in subagents:
        if agent.parent not in known:
            agent.parent = session_id
    return Session("Claude Code", session_id, path, orchestrator, subagents)


# Finding and reading sessions


def resolve(name: str, codex_home: Path, claude_home: Path) -> Path:
    path = Path(name)
    if path.is_file():
        return path
    found = sorted((codex_home / "sessions").glob(f"**/rollout-*-{name}.jsonl"))
    found += sorted((claude_home / "projects").glob(f"*/{name}.jsonl"))
    if len(found) == 1:
        return found[0]
    if not found:
        raise CycleStagesError(f"no transcript of session {name!r}")
    raise CycleStagesError(f"session {name!r} matches several transcripts: "
                           + ", ".join(str(p) for p in found))


def read_session(path: Path, codex_home: Path) -> Session:
    entry = first_line(path)
    if entry.get("type") == "session_meta":
        meta = entry.get("payload") or {}
        if meta.get("parent_thread_id"):
            raise CycleStagesError(f"{path} is a subagent's rollout, not an orchestrator's")
        return read_codex_session(path, codex_home)
    if "sessionId" in entry or "type" in entry:
        return read_claude_session(path)
    raise CycleStagesError(f"{path} is neither a Codex rollout nor a Claude Code transcript")


# Stages


def top_level(agent: Agent, by_key: dict[str, Agent], roots: set[str]) -> Agent:
    seen = set()
    while agent.parent not in roots and agent.parent in by_key and agent.key not in seen:
        seen.add(agent.key)
        agent = by_key[agent.parent]
    return agent


def merge(intervals: list[tuple[datetime, datetime]]) -> list[tuple[datetime, datetime]]:
    merged: list[tuple[datetime, datetime]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def overlap(intervals: list[tuple[datetime, datetime]], start: datetime | None,
            end: datetime | None) -> timedelta:
    total = timedelta()
    for a, b in intervals:
        lo = a if start is None else max(a, start)
        hi = b if end is None else min(b, end)
        if hi > lo:
            total += hi - lo
    return total


def add_model(models: list[str], model: str | None) -> None:
    if model and model not in models:
        models.append(model)


def build_rows(sessions: list[Session]) -> list[Row]:
    roots = {session.orchestrator.key for session in sessions}
    by_key = {agent.key: agent for session in sessions for agent in session.subagents}
    stages: dict[str, list[Row]] = {}
    for session in sessions:
        for agent in session.subagents:
            if agent.parent in roots:
                count = len(agent.turns)
                stages[agent.key] = [
                    Row(start, agent.name + (f" — turn {n}" if count > 1 else ""), end - start,
                        window=(start, end))
                    for n, (start, end) in enumerate(agent.turns, 1)
                ]
    owned = sorted(((record, top_level(agent, by_key, roots).key)
                    for session in sessions for agent in session.subagents
                    for record in agent.records), key=lambda pair: pair[0].at)
    for record, owner in owned:
        rows = stages.get(owner)
        if not rows:
            continue
        row = next((r for r in rows if r.window[0] <= record.at <= r.window[1]), None)
        if row is None:
            earlier = [r for r in rows if r.window[0] <= record.at]
            row = earlier[-1] if earlier else rows[0]
        row.subagent.add(record.usage)
        add_model(row.subagent_models, record.model)
    stage_rows = [row for rows in stages.values() for row in rows]
    busy = merge([row.window for row in stage_rows])
    active = merge([turn for session in sessions for turn in session.orchestrator.turns])
    edges = [None] + [point for block in busy for point in block] + [None]
    stretches = []
    for index in range(0, len(edges), 2):
        start, end = edges[index], edges[index + 1]
        stretches.append(Row(stretch_start(start, end, active), "orchestrator",
                             overlap(active, start, end), window=(start, end)))
    parallel: dict[frozenset[int], Row] = {}
    for session in sessions:
        for record in session.orchestrator.records:
            running = [i for i, row in enumerate(stage_rows)
                       if row.window[0] <= record.at <= row.window[1]]
            if len(running) == 1:
                row = stage_rows[running[0]]
            elif running:
                group = frozenset(running)
                if group not in parallel:
                    names = ", ".join(stage_rows[i].name for i in sorted(running))
                    parallel[group] = Row(record.at, f"orchestrator while in parallel: {names}",
                                          None)
                row = parallel[group]
            else:
                row = next(r for r in stretches
                           if (r.window[0] is None or r.window[0] < record.at)
                           and (r.window[1] is None or record.at < r.window[1]))
            row.orchestrator.add(record.usage)
            add_model(row.orchestrator_models, record.model)
    stretches = [row for row in stretches if row.duration or row.orchestrator.total]
    rows = stage_rows + stretches + list(parallel.values())
    rows.sort(key=lambda row: row.start)
    return rows


def stretch_start(start: datetime | None, end: datetime | None,
                  active: list[tuple[datetime, datetime]]) -> datetime:
    """Where an orchestrator stretch stands in time order: its start, or for the stretch before
    the first subagent turn the orchestrator's first turn."""
    if start is not None:
        return start
    first = min((a for a, _ in active), default=None)
    if first is not None and (end is None or first < end):
        return first
    return end if end is not None else datetime.min.replace(tzinfo=timezone.utc)


# Report


def duration_text(value: timedelta | None) -> str:
    if value is None:
        return "—"
    seconds = round(value.total_seconds())
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"


def number(value: int) -> str:
    return f"{value:,}"


def report(sessions: list[Session], rows: list[Row]) -> str:
    lines = ["# Stages of the cycle run", ""]
    for session in sessions:
        lines.append(f"- {session.tool} session `{session.id}`: {len(session.subagents)} "
                     f"subagents — `{session.path.name}`")
    lines += [
        "",
        "A stage is one turn of a subagent the orchestrator started, from its prompt to its "
        "answer, or a stretch of the orchestrator's own work between such turns. Durations are "
        "h:mm:ss; an orchestrator stretch counts only the time inside the orchestrator's turns, "
        "never the wait for the human. Tokens are input, which includes the part read from a "
        "cache, plus output, which includes reasoning.",
        "",
        "| # | Stage | Duration | Subagent model | Orchestrator model | Subagent tokens "
        "| Orchestrator tokens | Total tokens | Cached input | Output |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    totals = Usage()
    for index, row in enumerate(rows, 1):
        both = Usage()
        both.add(row.subagent)
        both.add(row.orchestrator)
        totals.add(both)
        lines.append(
            f"| {index} | {row.name.replace('|', '/')} | {duration_text(row.duration)} "
            f"| {', '.join(row.subagent_models) or '—'} "
            f"| {', '.join(row.orchestrator_models) or '—'} "
            f"| {number(row.subagent.total)} | {number(row.orchestrator.total)} "
            f"| {number(both.total)} | {number(both.cached)} | {number(both.output)} |")
    by_model: dict[str, Usage] = {}
    for session in sessions:
        for agent in [session.orchestrator, *session.subagents]:
            for record in agent.records:
                by_model.setdefault(record.model or "unknown", Usage()).add(record.usage)
    active = merge([turn for session in sessions for turn in session.orchestrator.turns]
                   + [row.window for row in rows if row.duration is not None
                      and row.name != "orchestrator"])
    lines += [
        "",
        f"- Working time, orchestrator turns and subagent turns joined: "
        f"{duration_text(overlap(active, None, None))}",
        f"- Tokens in all: {number(totals.total)} — cached input {number(totals.cached)}, "
        f"output {number(totals.output)}",
        "",
        "| Model | Total tokens | Input | Cached input | Output |",
        "|---|---|---|---|---|",
    ]
    for model, usage in sorted(by_model.items(), key=lambda item: -item[1].total):
        lines.append(f"| {model} | {number(usage.total)} | {number(usage.input)} "
                     f"| {number(usage.cached)} | {number(usage.output)} |")
    return "\n".join(lines) + "\n"


def default_home(variable: str, folder: str) -> Path:
    value = os.environ.get(variable)
    return Path(value) if value else Path.home() / folder


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("sessions", nargs="*", metavar="SESSION")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--codex-home", type=Path, default=default_home("CODEX_HOME", ".codex"))
    parser.add_argument("--claude-home", type=Path,
                        default=default_home("CLAUDE_CONFIG_DIR", ".claude"))
    args = parser.parse_args(argv)
    names = args.sessions or ([os.environ["CLAUDE_CODE_SESSION_ID"]]
                              if os.environ.get("CLAUDE_CODE_SESSION_ID") else [])
    try:
        if not names:
            raise CycleStagesError("name a session; CLAUDE_CODE_SESSION_ID is not set either")
        paths = dict.fromkeys(resolve(name, args.codex_home, args.claude_home).resolve()
                              for name in names)
        sessions = [read_session(path, args.codex_home) for path in paths]
        text = report(sessions, build_rows(sessions))
    except CycleStagesError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
