"""The stages of one run of the task cycle — how long each took, which models did it and how many
tokens it used — counted from the session transcripts that Codex and Claude Code keep.

Usage:

    python -B task-cycle/cycle_stages.py [SESSION ...] [--output PATH]
        [--codex-home DIR] [--claude-home DIR]

SESSION names one session of the cycle's orchestrator: the path of its transcript, or its id. A
Codex id is looked up as `<codex home>/sessions/**/rollout-*-<id>.jsonl`, a Claude Code id as
`<claude home>/projects/*/<id>.jsonl`. The homes default to the environment variables CODEX_HOME
and CLAUDE_CONFIG_DIR, and otherwise to `~/.codex` and `~/.claude`. Name every session of the run,
in any order. Without SESSION, the session running the command is taken: Claude Code names it in
CLAUDE_CODE_SESSION_ID and Codex in CODEX_SESSION_ID; where both are set, as in one tool started
from the other's terminal, SESSION has to be named.

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

A wait for a tool is the time from a tool call to its result in the transcript: from the entry that
starts the call to the entry that carries its result — in Claude Code, the `tool_use` block of an
assistant response to the `tool_result` block with its id; in Codex, the `function_call` or
`custom_tool_call` item to the output with its `call_id`. A call that starts a subagent, sends it a
message or waits for it is no wait for a tool, its time being the subagent's work. Those calls are
Claude Code's `Agent`, `Task` and `SendMessage`, and Codex's `spawn_agent`, `wait_agent`,
`send_message` and `followup_task`, each read from the `name` of its tool call. A Codex `exec` call
whose script calls one of the Codex subagent tools is left out of the waits, with a warning. A call
with no result that a later entry of its transcript follows — the result of any call, a message to
the agent, another response of its model, or in Codex the end of its turn — or a call of a type the
reader does not recognise, makes the waits of its stage and of the cycle `unknown`, with a warning,
and is never counted as a wait of zero. A call with no result that nothing of these follows, so that
its transcript ends while it runs, is no wait and makes nothing `unknown`: its time lies after the
agent's last entry, outside every working window. That is the call that runs this script on the
live session running it, in the orchestrator's transcript or a subagent's, and a call of a session
stopped while it ran. A call counts in the stage running when it starts, as its tokens do; the
cycle's waiting time counts each moment once, even where calls overlap.

The files a subagent turn was given: for each turn, the files of the cycle's `reports/` that the
message starting it names — its prompt, or the message that resumes it — read from the subagent's
transcript: in Claude Code the user line that starts the turn, in Codex the first message the
rollout gives the turn, the user's or another agent's addressed to it, past the AGENTS.md text and
the environment that Codex gives a turn first as user messages. A name counts where it follows the
folder `reports` and a separator, starts with a letter, a digit or `_`, holds only letters, digits,
`_`, `-` and `.`, holds no `..`, ends in `.md` and is at most 120 characters long, the full stops
that end a sentence after it left out; it is written as `reports/<name>`, each once, at most 20 per
turn, with a warning where a turn names more. The text is data: no path in it is followed. A message whose payload is encrypted,
as Codex writes another agent's message, or a turn with no message found, names files
`unknown`. The audit of the process ties a turn to the fix round whose findings file it names
(WAY-337). The column *Files named* is a form of this report of its own: the reports that hold it
start a series of the audit's measures apart from the earlier ones (WAY-339).

A stage with no token usage has the model `—` and zero counts in the section of the stages where
its agent's transcript holds token usage elsewhere; where that transcript holds none at all, so that
its usage was not read, the model reads `unknown` — for the orchestrator's rows, where any of the
orchestrator's transcripts holds none.

The report is Markdown, written to PATH or printed. It lists, and prints on stderr as `Warning:`
lines, what suggests that a transcript was not read as its tool writes it — a session or a
subagent with no turn or no token usage, a response naming no model, a Codex subagent turn with no
`task_complete`, a Claude Code subagent with no `.meta.json`, a call with no result or of an
unrecognised type — since a line the reader no longer recognises is skipped and its tokens and
waits go uncounted. Exit code: 0 on success, warnings included; 1 with `Error: <message>` on stderr
otherwise.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
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
class Call:
    """A tool call from its start to its result. `end` is None where no result was read; `known`
    is False where the reader does not recognise the call's type."""
    start: datetime
    end: datetime | None
    name: str
    known: bool = True

    @property
    def readable(self) -> bool:
        return self.end is not None and self.end >= self.start


@dataclass
class Agent:
    key: str
    name: str
    parent: str | None
    turns: list[tuple[datetime, datetime]] = field(default_factory=list)
    # For each turn, the files of `reports/` the message that starts it names, or None where that
    # message cannot be read.
    turn_files: list[list[str] | None] = field(default_factory=list)
    records: list[Record] = field(default_factory=list)
    calls: list[Call] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


# Tool calls that start a subagent, send it a message or wait for it: their time is the subagent's
# work, so they are no wait for a tool.
CLAUDE_SUBAGENT_CALLS = frozenset({"Agent", "Task", "SendMessage"})
CODEX_SUBAGENT_CALLS = frozenset({"spawn_agent", "wait_agent", "send_message", "followup_task"})
CODEX_SUBAGENT_USE = re.compile(r"tools\.(?:" + "|".join(sorted(CODEX_SUBAGENT_CALLS)) + r")\b")
CODEX_CALL_KINDS = frozenset({"function_call", "custom_tool_call"})


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
    calls: list[Call] = field(default_factory=list)
    by_model: dict[str, Usage] = field(default_factory=dict)
    named: list[str] | None = field(default_factory=list)
    # False where the transcript the row's usage comes from holds no token usage at all.
    usage_read: bool = True


# A file of the cycle's `reports/` named in the message that starts a subagent turn: the folder
# `reports` after a separator, and a name of letters, digits, `_`, `-` and `.` ending in `.md`.
# The run of name characters is taken whole, so no crafted text makes the pattern try again.
FILE_NAMED = re.compile(r"(?<![A-Za-z0-9_.-])reports[\\/]+([A-Za-z0-9_.-]+)")
MAX_FILE_NAME = 120
MAX_FILES_NAMED = 20


def files_named(text: str) -> tuple[list[str], bool]:
    """The files of `reports/` that `text` names, as `reports/<name>`, each once in the order
    first named, and whether more than MAX_FILES_NAMED were named. The full stops that end a name
    are cut. Text from a transcript is data: a name that starts with neither a letter, a digit nor
    `_`, holds `..`, does not end in `.md` or is longer than MAX_FILE_NAME is left out, and no path
    is followed."""
    found: list[str] = []
    for match in FILE_NAMED.finditer(text):
        # A full stop after the name ends the sentence the name stands in; it is no part of it.
        name = match.group(1).rstrip(".")
        if (len(name) > MAX_FILE_NAME or not name.endswith(".md") or ".." in name
                or not (name[0].isalnum() or name[0] == "_")):
            continue
        path = f"reports/{name}"
        if path in found:
            continue
        if len(found) == MAX_FILES_NAMED:
            return found, True
        found.append(path)
    return found, False


def add_named_note(agent: Agent, over: int) -> None:
    """A warning for the subagent turns that named more files than the column keeps; the
    orchestrator's own messages fill no column."""
    if over and agent.parent is not None:
        agent.notes.append(f"{over} turn(s) name more than {MAX_FILES_NAMED} files of `reports/`; "
                           "the rest are left out of *Files named*")


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


def add_calls(agent: Agent, started: dict[str, tuple[datetime, str]],
              ended: dict[str, datetime], tail: set[str]) -> None:
    """The agent's calls, each with its result. A call with no result in `tail`, which no later
    entry of the transcript follows, is cut off by the end of the transcript: it is no wait, so it
    ends where it starts."""
    for key, (start, call_name) in started.items():
        end = ended.get(key)
        if end is None and key in tail:
            end = start
        agent.calls.append(Call(start, end, call_name))


def add_call_notes(agent: Agent) -> None:
    """Warnings for the calls whose waits cannot be known: no readable result, or a type the reader
    does not recognise."""
    unpaired = sum(1 for call in agent.calls if call.known and not call.readable)
    if unpaired:
        agent.notes.append(f"{unpaired} tool call(s) with no readable result: their waits are "
                           "unknown")
    unrecognised = [call.name for call in agent.calls if not call.known]
    if unrecognised:
        agent.notes.append(f"{len(unrecognised)} call(s) of a type the reader does not recognise "
                           f"({', '.join(sorted(set(unrecognised)))}): their waits are unknown")


# Codex


def codex_meta(path: Path) -> dict | None:
    entry = first_line(path)
    if entry.get("type") != "session_meta":
        return None
    return entry.get("payload") or {}


def codex_message_text(payload: dict, own_path: str | None) -> tuple[bool, str | None]:
    """Whether a rollout item is a message sent to the agent — the user's message, or another
    agent's message addressed to it — and its text, or None where a part of it is encrypted. The
    parts Codex injects are left out, and a message of nothing else is none."""
    item = payload.get("type")
    if item == "message" and payload.get("role") == "user":
        parts = payload.get("content")
    elif item == "agent_message" and own_path and payload.get("recipient") == own_path:
        parts = payload.get("content")
    else:
        return False, None
    texts = []
    injected = False
    for part in parts if isinstance(parts, list) else []:
        if not isinstance(part, dict):
            continue
        if part.get("type") == "encrypted_content":
            return True, None
        if isinstance(part.get("text"), str):
            if is_injected(part["text"]):
                injected = True
            else:
                texts.append(part["text"])
    if injected and not texts:
        # Only what Codex gives the turn first: no message that sets the agent working.
        return False, None
    return True, "\n".join(texts)


# The texts Codex gives a turn first as user messages, before the message that sets it working:
# the AGENTS.md text and the environment, each opening with its mark.
CODEX_INJECTED = ("# AGENTS.md instructions", "<environment_context>", "<user_instructions>")


def is_injected(text: str) -> bool:
    return text.lstrip().startswith(CODEX_INJECTED)


def read_codex_agent(path: Path, parent: str | None) -> Agent:
    meta = codex_meta(path)
    if meta is None:
        raise CycleStagesError(f"{path} does not start with a Codex session_meta line")
    own = meta["id"]
    name = meta.get("agent_path") or meta.get("agent_nickname") or own
    # The message that starts each turn, as its text, or None where it cannot be read; the turn a
    # message belongs to is the one it names, or else the last turn started before it.
    messages: dict[str, str | None] = {}
    current: str | None = None
    starts: dict[str, datetime] = {}
    ends: dict[str, datetime] = {}
    first_seen: dict[str, datetime] = {}
    last_seen: dict[str, datetime] = {}
    models: dict[str, str] = {}
    own_turns: set[str] = set()
    raw: list[tuple[datetime, str, dict]] = []
    started_calls: dict[str, tuple[datetime, str]] = {}
    finished_calls: dict[str, datetime] = {}
    # The calls started since the last entry that shows the agent went on: an output, a message,
    # another item of a response, or a turn starting or ending.
    tail: set[str] = set()
    unrecognised: list[Call] = []
    left_out = 0
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
            if event in ("task_started", "user_message", "task_complete"):
                tail.clear()
            if event == "task_started":
                starts.setdefault(turn, at)
                current = turn or current
            elif event == "user_message":
                owner = turn or current
                text = payload.get("message")
                if owner and owner not in messages and not (
                        isinstance(text, str) and is_injected(text)):
                    messages[owner] = text if isinstance(text, str) else None
            elif event == "task_complete":
                ends[turn] = at
            elif event == "item_completed" and payload.get("thread_id") == own:
                own_turns.add(turn)
        elif kind == "turn_context" and turn:
            models[turn] = payload.get("model")
        elif kind == "response_item":
            item = str(payload.get("type") or "")
            ident = payload.get("call_id")
            if item not in CODEX_CALL_KINDS:
                tail.clear()
            is_message, text = codex_message_text(payload, meta.get("agent_path"))
            if is_message:
                passthrough = payload.get("internal_chat_message_metadata_passthrough")
                owner = (passthrough.get("turn_id") if isinstance(passthrough, dict) else None) \
                    or current
                if owner and owner not in messages:
                    messages[owner] = text
            elif item in CODEX_CALL_KINDS:
                call_name = str(payload.get("name") or item)
                if call_name in CODEX_SUBAGENT_CALLS:
                    continue
                script = str(payload.get("input") or "")
                if call_name == "exec" and CODEX_SUBAGENT_USE.search(script):
                    left_out += 1
                    continue
                key = ident or f"no call id {len(started_calls)}"
                started_calls.setdefault(key, (at, call_name))
                tail.add(key)
            elif item.endswith("_call_output"):
                if ident:
                    finished_calls.setdefault(ident, at)
            elif item.endswith("_call"):
                unrecognised.append(Call(at, None, item, known=False))
        elif kind == "token_usage_record" and payload.get("thread_id") == own:
            own_turns.add(turn)
            raw.append((at, turn, payload.get("usage") or {}))
    # A forked subagent's rollout repeats its parent's history; only turns that the subagent's
    # own thread worked in are its turns.
    agent = Agent(own, name, parent)
    turns = []
    over = 0
    for turn in own_turns:
        start = starts.get(turn) or first_seen[turn]
        text = messages.get(turn)
        named = None
        if text is not None:
            named, cut = files_named(text)
            over += cut
        turns.append((start, ends.get(turn) or last_seen[turn], named))
    open_turns = len(own_turns - ends.keys())
    if open_turns and parent is not None:
        agent.notes.append(f"{open_turns} turn(s) without `task_complete`, each ending at its "
                           "last entry")
    add_named_note(agent, over)
    turns.sort(key=lambda turn: turn[:2])
    agent.turns = [(start, end) for start, end, _ in turns]
    agent.turn_files = [named for _, _, named in turns]
    add_calls(agent, started_calls, finished_calls, tail)
    agent.calls.extend(unrecognised)
    if parent is not None:
        # A forked subagent's rollout repeats its parent's calls before its own turns.
        agent.calls = [call for call in agent.calls
                       if any(a <= call.start <= b for a, b in agent.turns)]
    if left_out:
        agent.notes.append(f"{left_out} exec call(s) that call a subagent tool: their time is "
                           "left out of the waits")
    add_call_notes(agent)
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


def content_blocks(entry: dict) -> list[dict]:
    """The blocks of a message's content list; a text content gives none."""
    content = (entry.get("message") or {}).get("content")
    if not isinstance(content, list):
        return []
    return [block for block in content if isinstance(block, dict)]


def message_text(entry: dict) -> str:
    """The text of a user line: its content as a string, or its text blocks joined."""
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return content
    return "\n".join(block["text"] for block in content_blocks(entry)
                     if block.get("type") == "text" and isinstance(block.get("text"), str))


def read_claude_agent(path: Path, key: str, name: str, parent: str | None) -> Agent:
    responses: dict[str, tuple[datetime, dict, str | None]] = {}
    # Each line that sets the agent working, with the files of `reports/` it names.
    prompts: list[tuple[datetime, list[str]]] = []
    over = 0
    activity: list[datetime] = []
    answered = True
    started_calls: dict[str, tuple[datetime, str]] = {}
    results: dict[str, datetime] = {}
    # The calls of the last response, while no user line and no other response follows it.
    tail: set[str] = set()
    tail_response: object = None
    unrecognised: list[Call] = []
    for entry in read_lines(path):
        if "timestamp" not in entry:
            continue
        at = parse_time(entry["timestamp"])
        if entry.get("type") == "user":
            tail.clear()
            for block in content_blocks(entry):
                if block.get("type") == "tool_result":
                    results.setdefault(block.get("tool_use_id"), at)
            # Text the human types, or a notice, sets the agent working; text the tool adds
            # (a loaded skill, a message from the coordinator) does so only once the agent has
            # answered, and is part of the running turn otherwise.
            if is_text(entry) and (not entry.get("isMeta") or answered):
                named, cut = files_named(message_text(entry))
                over += cut
                prompts.append((at, named))
                answered = False
            else:
                activity.append(at)
        elif entry.get("type") == "assistant":
            message = entry.get("message") or {}
            model = message.get("model")
            if model == "<synthetic>":
                continue
            activity.append(at)
            # Claude Code writes one response over several lines, which share its id.
            ident = message.get("id") or entry.get("uuid")
            if ident != tail_response:
                tail.clear()
                tail_response = ident
            for block in content_blocks(entry):
                kind = str(block.get("type") or "")
                call_name = str(block.get("name") or "")
                if kind == "tool_use" and call_name in CLAUDE_SUBAGENT_CALLS:
                    continue
                if kind == "tool_use" and block.get("id"):
                    started_calls.setdefault(block["id"], (at, call_name or kind))
                    tail.add(block["id"])
                elif kind == "tool_use" or kind.endswith("_tool_use"):
                    unrecognised.append(Call(at, None, call_name or kind, known=False))
            if message.get("stop_reason"):
                answered = message["stop_reason"] == "end_turn"
            usage = message.get("usage") or {}
            kept = responses.get(ident)
            if kept is None or usage.get("output_tokens", 0) >= kept[1].get("output_tokens", 0):
                responses[ident] = (at, usage, model)
    agent = Agent(key, name, parent)
    add_calls(agent, started_calls, results, tail)
    agent.calls.extend(unrecognised)
    add_call_notes(agent)
    prompts.sort(key=lambda prompt: prompt[0])
    activity.sort()
    for index, (start, named) in enumerate(prompts):
        stop = prompts[index + 1][0] if index + 1 < len(prompts) else None
        inside = [at for at in activity if at >= start and (stop is None or at < stop)]
        if inside:
            agent.turns.append((start, inside[-1]))
            agent.turn_files.append(named)
    add_named_note(agent, over)
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
            notes = []
            if not meta_path.is_file():
                notes.append(f"no `{meta_path.name}`, so it is named by its id")
            else:
                try:
                    meta = json.loads(meta_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as error:
                    raise CycleStagesError(f"cannot read {meta_path}: {error}") from error
            description = meta.get("description") or agent_id
            kind = meta.get("agentType")
            name = f"{description} ({kind})" if kind else description
            subagent = read_claude_agent(
                transcript, agent_id, name, meta.get("parentAgentId") or session_id)
            subagent.notes.extend(notes)
            subagents.append(subagent)
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


def add_by_model(row: Row, usage: Usage, model: str | None) -> None:
    row.by_model.setdefault(model or "unknown", Usage()).add(usage)


def stage_row(rows: list[Row], at: datetime) -> Row:
    """The stage a subagent's work at a moment is counted in: the turn running then, or else the
    last turn started before it."""
    row = next((r for r in rows if r.window[0] <= at <= r.window[1]), None)
    if row is None:
        earlier = [r for r in rows if r.window[0] <= at]
        row = earlier[-1] if earlier else rows[0]
    return row


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
                        window=(start, end), named=named, usage_read=bool(agent.records))
                    for n, ((start, end), named) in enumerate(
                        zip(agent.turns, agent.turn_files), 1)
                ]
    owned = sorted(((record, top_level(agent, by_key, roots).key)
                    for session in sessions for agent in session.subagents
                    for record in agent.records), key=lambda pair: pair[0].at)
    for record, owner in owned:
        rows = stages.get(owner)
        if not rows:
            continue
        row = stage_row(rows, record.at)
        row.subagent.add(record.usage)
        add_model(row.subagent_models, record.model)
        add_by_model(row, record.usage, record.model)
    for session in sessions:
        for agent in session.subagents:
            rows = stages.get(top_level(agent, by_key, roots).key)
            if not rows:
                continue
            for call in agent.calls:
                stage_row(rows, call.start).calls.append(call)
    stage_rows = [row for rows in stages.values() for row in rows]
    busy = merge([row.window for row in stage_rows])
    active = merge([turn for session in sessions for turn in session.orchestrator.turns])
    edges = [None] + [point for block in busy for point in block] + [None]
    orchestrator_read = all(session.orchestrator.records for session in sessions)
    stretches = []
    for index in range(0, len(edges), 2):
        start, end = edges[index], edges[index + 1]
        stretches.append(Row(stretch_start(start, end, active), "orchestrator",
                             overlap(active, start, end), window=(start, end),
                             usage_read=orchestrator_read))
    parallel: dict[frozenset[int], Row] = {}

    def orchestrator_row(at: datetime) -> Row:
        """The row the orchestrator's work at a moment is counted in: the stage running then, the
        row of the stages running together, or the orchestrator's stretch between stages."""
        running = [i for i, row in enumerate(stage_rows)
                   if row.window[0] <= at <= row.window[1]]
        if len(running) == 1:
            return stage_rows[running[0]]
        if running:
            group = frozenset(running)
            if group not in parallel:
                names = ", ".join(stage_rows[i].name for i in sorted(running))
                parallel[group] = Row(at, f"orchestrator while in parallel: {names}", None,
                                      usage_read=orchestrator_read)
            return parallel[group]
        return next(r for r in stretches
                    if (r.window[0] is None or r.window[0] < at)
                    and (r.window[1] is None or at < r.window[1]))

    for session in sessions:
        for record in session.orchestrator.records:
            row = orchestrator_row(record.at)
            row.orchestrator.add(record.usage)
            add_model(row.orchestrator_models, record.model)
            add_by_model(row, record.usage, record.model)
        for call in session.orchestrator.calls:
            orchestrator_row(call.start).calls.append(call)
    stretches = [row for row in stretches if row.duration or row.orchestrator.total or row.calls]
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


def find_warnings(sessions: list[Session]) -> list[str]:
    """What suggests that a transcript was not read as its tool writes it: the counts beside such
    a warning may be short, since a reader that no longer recognises a line skips it."""
    found = []
    for session in sessions:
        orchestrator = session.orchestrator
        where = f"{session.tool} session `{session.id}`"
        if not orchestrator.turns:
            found.append(f"{where}: the orchestrator's transcript holds no turn")
        if not orchestrator.records:
            found.append(f"{where}: the orchestrator's transcript holds no token usage")
        for agent in [orchestrator, *session.subagents]:
            label = f"{where}, {'the orchestrator' if agent is orchestrator else agent.name}"
            if agent is not orchestrator:
                if not agent.turns:
                    found.append(f"{label}: no turn found")
                if not agent.records:
                    found.append(f"{label}: no token usage found")
            unnamed = sum(1 for record in agent.records if not record.model)
            if unnamed:
                found.append(f"{label}: {unnamed} response(s) name no model")
            found.extend(f"{label}: {note}" for note in agent.notes)
    return found


def duration_text(value: timedelta | None) -> str:
    if value is None:
        return "—"
    seconds = round(value.total_seconds())
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"


def one_line(text: str) -> str:
    """Transcript text on one line, so that it cannot break a list or a table."""
    return " ".join(text.split())


def cell(text: str) -> str:
    return one_line(text).replace("|", "/")


def clock_text(at: datetime) -> str:
    return at.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def wait_text(calls: list[Call]) -> str:
    """A stage's time waiting for tools, or `unknown` with the time known so far where a call's
    result is missing or its type is not recognised."""
    known = merge([(call.start, call.end) for call in calls if call.readable])
    total = overlap(known, None, None)
    if any(not call.readable for call in calls):
        return f"unknown (at least {duration_text(total)})"
    return duration_text(total)


def wait_totals(rows: list[Row], active: list[tuple[datetime, datetime]]) -> tuple[timedelta, int]:
    """The cycle's time waiting for tools, each moment counted once and within the working time,
    and the number of calls whose wait is unknown."""
    calls = [call for row in rows for call in row.calls]
    known = merge([(call.start, call.end) for call in calls if call.readable])
    waiting = sum((overlap(active, start, end) for start, end in known), timedelta())
    return waiting, sum(1 for call in calls if not call.readable)


def number(value: int) -> str:
    return f"{value:,}"


def report(sessions: list[Session], rows: list[Row], warnings: list[str]) -> str:
    lines = ["# Stages of the cycle run", ""]
    for session in sessions:
        lines.append(f"- {session.tool} session `{session.id}`: {len(session.subagents)} "
                     f"subagents — `{session.path.name}`")
    lines += ["", "Warnings:" if warnings else "Warnings: none."]
    lines += [f"- {one_line(warning)}" for warning in warnings]
    lines += [
        "",
        "A stage is one turn of a subagent the orchestrator started, from its prompt to its "
        "answer, or a stretch of the orchestrator's own work between such turns. Durations are "
        "h:mm:ss; an orchestrator stretch counts only the time inside the orchestrator's turns, "
        "never the wait for the human. Tokens are input, which includes the part read from a "
        "cache, plus output, which includes reasoning.",
        "",
        "Waiting for tools is the time of the stage's tool calls, not of its subagents' calls; "
        "see the section on the stages below.",
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
            f"| {index} | {cell(row.name)} | {duration_text(row.duration)} "
            f"| {cell(', '.join(row.subagent_models)) or '—'} "
            f"| {cell(', '.join(row.orchestrator_models)) or '—'} "
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
    working = overlap(active, None, None)
    waiting, unknown = wait_totals(rows, active)
    if unknown:
        waiting_lines = [
            f"- Waiting for tools: unknown — at least {duration_text(waiting)}; {unknown} "
            "call(s) with no readable result or of a type not recognised, see Warnings",
            f"- Working time without waiting for tools: unknown — at most "
            f"{duration_text(working - waiting)}",
        ]
    else:
        waiting_lines = [
            f"- Waiting for tools: {duration_text(waiting)}",
            f"- Working time without waiting for tools: {duration_text(working - waiting)}",
        ]
    lines += [
        "",
        f"- Working time, orchestrator turns and subagent turns joined: "
        f"{duration_text(working)}",
        *waiting_lines,
        f"- Tokens in all: {number(totals.total)} — cached input {number(totals.cached)}, "
        f"output {number(totals.output)}",
        "",
        "| Model | Total tokens | Input | Cached input | Output |",
        "|---|---|---|---|---|",
    ]
    for model, usage in sorted(by_model.items(), key=lambda item: -item[1].total):
        lines.append(f"| {cell(model)} | {number(usage.total)} | {number(usage.input)} "
                     f"| {number(usage.cached)} | {number(usage.output)} |")
    lines += [
        "",
        "## Stages: start, waiting for tools and tokens by model",
        "",
        "Times are UTC. Each stage's waiting for tools is the time of its tool calls, from each "
        "call to its result; `unknown` marks a stage with a call whose result was not read or "
        "whose type is not recognised. Input includes the part read from a cache. The model `—` "
        "marks a stage with no token usage, and `unknown` with zero counts one whose transcript "
        "holds no token usage at all, so that its usage was not read. *Files named* "
        "lists the files of the cycle's `reports/` that the message starting a subagent turn "
        "names — its prompt, or the message that resumes it — each once; it is empty where that "
        "message names none and for the orchestrator's rows, and `unknown` where the message "
        "cannot be read.",
        "",
        "| # | Stage | Start | Waiting for tools | Model | Input | Cached input | Output "
        "| Files named |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for index, row in enumerate(rows, 1):
        models = (sorted(row.by_model.items(), key=lambda item: -item[1].total)
                  or [("—" if row.usage_read else "unknown", Usage())])
        named = "unknown" if row.named is None else cell(", ".join(row.named))
        for model, usage in models:
            lines.append(f"| {index} | {cell(row.name)} | {clock_text(row.start)} "
                         f"| {wait_text(row.calls)} | {cell(model)} | {number(usage.input)} "
                         f"| {number(usage.cached)} | {number(usage.output)} | {named} |")
    return "\n".join(lines) + "\n"


SESSION_VARIABLES = ("CLAUDE_CODE_SESSION_ID", "CODEX_SESSION_ID")


def default_home(variable: str, folder: str) -> Path:
    value = os.environ.get(variable)
    return Path(value) if value else Path.home() / folder


def current_session() -> str:
    """The id of the session running this command, from the variable its tool sets."""
    found = {name: os.environ[name] for name in SESSION_VARIABLES if os.environ.get(name)}
    if len(found) == 1:
        return next(iter(found.values()))
    if not found:
        raise CycleStagesError("name a session; neither " + " nor ".join(SESSION_VARIABLES)
                               + " is set")
    # A tool started from the other's terminal inherits its variable.
    raise CycleStagesError("name a session; both " + " and ".join(SESSION_VARIABLES)
                           + " are set")


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
        sessions = [read_session(path, args.codex_home) for path in paths]
        warnings = find_warnings(sessions)
        text = report(sessions, build_rows(sessions), warnings)
    except CycleStagesError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
