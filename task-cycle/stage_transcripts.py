"""The reading of the session transcripts of the task cycle, moved out of `cycle_stages.py`.

The reading of the transcripts that Codex and Claude Code keep of a session and of its subagents
(`read_session`, `read_codex_session`, `read_claude_session`), the classes it fills (`Session`,
`Agent`, `Record`, `Call`, `Usage`), the errors it ends with (`CycleStagesError`,
`MissingFieldError`) and the reading of the files that a message names (`files_named`), as
`task-cycle/cycle_stages.py` counts the stages of a cycle from them (WAY-48). The description of
that script holds which fields the reading needs and how it ends where one is missing. It is
imported, never run, and runs nothing when imported. Standard library only.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


class CycleStagesError(Exception):
    """A session that cannot be found or read."""


class MissingFieldError(CycleStagesError):
    """A transcript or rollout that lacks a field the reading needs, or holds one of the wrong
    kind."""


@dataclass
class Usage:
    input: int = 0
    cached: int = 0
    output: int = 0
    # The cache writes of each lifetime, parts of `input`; a Codex record gives none, so 0.
    write_5m: int = 0
    write_1h: int = 0

    def add(self, other: Usage) -> None:
        self.input += other.input
        self.cached += other.cached
        self.output += other.output
        self.write_5m += other.write_5m
        self.write_1h += other.write_1h

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
        if (
            len(name) > MAX_FILE_NAME
            or not name.endswith(".md")
            or ".." in name
            or not (name[0].isalnum() or name[0] == "_")
        ):
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
        agent.notes.append(
            f"{over} turn(s) name more than {MAX_FILES_NAMED} files of `reports/`; "
            "the rest are left out of *Files named*"
        )


def parse_time(text: str) -> datetime:
    return datetime.fromisoformat(text)


def numbered_lines(path: Path):
    """Each non-blank line of a JSON Lines file as its number in the file and its value. A line that
    is not JSON, is nested too deep or holds a number of too many digits ends the reading, as does
    a file that cannot be read or is no UTF-8."""
    try:
        with path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if line.strip():
                    try:
                        yield number, json.loads(line)
                    except (ValueError, RecursionError, MemoryError) as error:
                        raise CycleStagesError(f"{path}:{number}: not JSON: {error}") from error
    except (OSError, UnicodeDecodeError) as error:
        raise CycleStagesError(f"cannot read {path}: {error}") from error


def read_lines(path: Path):
    for _, entry in numbered_lines(path):
        yield entry


def first_line(path: Path) -> dict:
    for entry in read_lines(path):
        return entry
    raise CycleStagesError(f"{path} is empty")


def add_calls(
    agent: Agent,
    started: dict[str, tuple[datetime, str]],
    ended: dict[str, datetime],
    tail: set[str],
) -> None:
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
        agent.notes.append(
            f"{unpaired} tool call(s) with no readable result: their waits are unknown"
        )
    unrecognised = [call.name for call in agent.calls if not call.known]
    if unrecognised:
        agent.notes.append(
            f"{len(unrecognised)} call(s) of a type the reader does not recognise "
            f"({', '.join(sorted(set(unrecognised)))}): their waits are unknown"
        )


# Fields a reading needs


def required(holder: object, key: str, name: str, where: str) -> object:
    """The value of a needed field; a missing field, which a `null` is, ends the reading, naming
    `where` and the field's `name`."""
    value = holder.get(key) if isinstance(holder, dict) else None
    if value is None:
        raise MissingFieldError(f"{where}: no field {name}")
    return value


# A token count longer than this is not a count of tokens: no model's input comes near it. The audit
# bounds the same counts alike (`TOKEN_DIGITS` of process-audit/audit_count.py), and a longer one
# would end the report with a stack trace where the sums of it are written out.
TOKEN_DIGITS = 15


def required_count(holder: object, key: str, name: str, where: str) -> int:
    value = required(holder, key, name, where)
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or value < 0
        or value >= 10**TOKEN_DIGITS
    ):
        raise MissingFieldError(f"{where}: field {name} is not a whole number")
    return value


def required_text(holder: object, key: str, name: str, where: str) -> str:
    """The value of a needed field that has to be a text, not empty."""
    value = required(holder, key, name, where)
    if not isinstance(value, str) or not value:
        raise MissingFieldError(f"{where}: field {name} is not a text")
    return value


def required_time(entry: dict, where: str) -> datetime:
    """The time of a line, in UTC; a naive time is taken as UTC."""
    value = required(entry, "timestamp", "timestamp", where)
    if not isinstance(value, str):
        raise MissingFieldError(f"{where}: field timestamp is not a time")
    try:
        at = parse_time(value)
        return (at if at.tzinfo else at.replace(tzinfo=timezone.utc)).astimezone(timezone.utc)
    except (ValueError, OverflowError) as error:
        raise MissingFieldError(f"{where}: field timestamp is not a time") from error


# Codex


def codex_meta(path: Path) -> dict | None:
    """The `payload` of the first line of a rollout where that is its `session_meta`, which has to
    give the `id` of the session as a text; None for a rollout that starts otherwise."""
    for number, entry in numbered_lines(path):
        break
    else:
        raise CycleStagesError(f"{path} is empty")
    if entry.get("type") != "session_meta":
        return None
    meta = entry.get("payload") or {}
    required_text(meta, "id", "payload.id", f"{path}:{number}")
    return meta


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


def codex_usage(payload: dict, where: str) -> Usage:
    """The tokens of a record of tokens of a Codex rollout, which `where` names by its file and
    line. The record's `usage` and each of its three counts are needed; one that is missing, or a
    count that is no whole number, ends the reading."""
    usage = required(payload, "usage", "payload.usage", where)
    return Usage(
        required_count(usage, "input_tokens", "payload.usage.input_tokens", where),
        required_count(usage, "cached_input_tokens", "payload.usage.cached_input_tokens", where),
        required_count(usage, "output_tokens", "payload.usage.output_tokens", where),
    )


def codex_tokens(payload: dict, own: str, where: str) -> tuple[str, Usage] | None:
    """The turn and the tokens of a record of tokens that belongs to the thread `own`, or None for
    a record of another thread. The record's `thread_id` is needed to tell the two apart, and
    the `turn_id` of the agent's own."""
    if required_text(payload, "thread_id", "payload.thread_id", where) != own:
        return None
    return required_text(payload, "turn_id", "payload.turn_id", where), codex_usage(payload, where)


@dataclass
class CodexScan:
    """What the lines of one Codex rollout hold of its agent, before the agent is built from them."""

    own: str
    agent_path: str | None
    # The message that starts each turn, as its text, or None where it cannot be read; the turn a
    # message belongs to is the one it names, or else the last turn started before it.
    messages: dict[str, str | None] = field(default_factory=dict)
    current: str | None = None
    starts: dict[str, datetime] = field(default_factory=dict)
    ends: dict[str, datetime] = field(default_factory=dict)
    first_seen: dict[str, datetime] = field(default_factory=dict)
    last_seen: dict[str, datetime] = field(default_factory=dict)
    models: dict[str, str] = field(default_factory=dict)
    own_turns: set[str] = field(default_factory=set)
    raw: list[tuple[datetime, str, Usage]] = field(default_factory=list)
    started_calls: dict[str, tuple[datetime, str]] = field(default_factory=dict)
    finished_calls: dict[str, datetime] = field(default_factory=dict)
    # The calls started since the last entry that shows the agent went on: an output, a message,
    # another item of a response, or a turn starting or ending.
    tail: set[str] = field(default_factory=set)
    unrecognised: list[Call] = field(default_factory=list)
    left_out: int = 0

    def read_event(self, payload: dict, turn: str | None, at: datetime) -> None:
        """A line of the kind `event_msg`: a turn starting, a message that sets it working, a turn
        ending, or an item of the agent's own thread."""
        event = payload.get("type")
        if event in ("task_started", "user_message", "task_complete"):
            self.tail.clear()
        if event == "task_started":
            self.starts.setdefault(turn, at)
            self.current = turn or self.current
        elif event == "user_message":
            owner = turn or self.current
            text = payload.get("message")
            if (
                owner
                and owner not in self.messages
                and not (isinstance(text, str) and is_injected(text))
            ):
                self.messages[owner] = text if isinstance(text, str) else None
        elif event == "task_complete":
            self.ends[turn] = at
        elif event == "item_completed" and payload.get("thread_id") == self.own:
            self.own_turns.add(turn)

    def read_response_item(self, payload: dict, at: datetime) -> None:
        """A line of the kind `response_item`: a message to the agent, a tool call, the output of
        one, or an item the reader does not recognise."""
        item = str(payload.get("type") or "")
        ident = payload.get("call_id")
        if item not in CODEX_CALL_KINDS:
            self.tail.clear()
        is_message, text = codex_message_text(payload, self.agent_path)
        if is_message:
            passthrough = payload.get("internal_chat_message_metadata_passthrough")
            owner = (passthrough.get("turn_id") if isinstance(passthrough, dict) else None) or (
                self.current
            )
            if owner and owner not in self.messages:
                self.messages[owner] = text
        elif item in CODEX_CALL_KINDS:
            call_name = str(payload.get("name") or item)
            if call_name in CODEX_SUBAGENT_CALLS:
                return
            script = str(payload.get("input") or "")
            if call_name == "exec" and CODEX_SUBAGENT_USE.search(script):
                self.left_out += 1
                return
            key = ident or f"no call id {len(self.started_calls)}"
            self.started_calls.setdefault(key, (at, call_name))
            self.tail.add(key)
        elif item.endswith("_call_output"):
            if ident:
                self.finished_calls.setdefault(ident, at)
        elif item.endswith("_call"):
            self.unrecognised.append(Call(at, None, item, known=False))

    def turns(self) -> tuple[list[tuple[datetime, datetime, list[str] | None]], int]:
        """The turns the agent's own thread worked in, each with its start, its end and the files
        its message names, in time order, and the number of turns that name more files than the
        column keeps. A forked subagent's rollout repeats its parent's history; only turns that the
        subagent's own thread worked in are its turns."""
        turns = []
        over = 0
        for turn in self.own_turns:
            start = self.starts.get(turn) or self.first_seen[turn]
            text = self.messages.get(turn)
            named = None
            if text is not None:
                named, cut = files_named(text)
                over += cut
            turns.append((start, self.ends.get(turn) or self.last_seen[turn], named))
        turns.sort(key=lambda turn: turn[:2])
        return turns, over


def codex_agent(scan: CodexScan, name: str, parent: str | None) -> Agent:
    """The agent that the lines of its rollout, read into `scan`, describe: its turns, its calls
    and its tokens, and the warnings for what the reading could not settle."""
    agent = Agent(scan.own, name, parent)
    turns, over = scan.turns()
    open_turns = len(scan.own_turns - scan.ends.keys())
    if open_turns and parent is not None:
        agent.notes.append(
            f"{open_turns} turn(s) without `task_complete`, each ending at its last entry"
        )
    add_named_note(agent, over)
    agent.turns = [(start, end) for start, end, _ in turns]
    agent.turn_files = [named for _, _, named in turns]
    add_calls(agent, scan.started_calls, scan.finished_calls, scan.tail)
    agent.calls.extend(scan.unrecognised)
    if parent is not None:
        # A forked subagent's rollout repeats its parent's calls before its own turns.
        agent.calls = [
            call for call in agent.calls if any(a <= call.start <= b for a, b in agent.turns)
        ]
    if scan.left_out:
        agent.notes.append(
            f"{scan.left_out} exec call(s) that call a subagent tool: their time is "
            "left out of the waits"
        )
    add_call_notes(agent)
    for at, turn, usage in scan.raw:
        agent.records.append(Record(at, usage, scan.models.get(turn)))
    return agent


def read_codex_agent(path: Path, parent: str | None) -> Agent:
    meta = codex_meta(path)
    if meta is None:
        raise CycleStagesError(f"{path} does not start with a Codex session_meta line")
    own = meta["id"]
    name = meta.get("agent_path") or meta.get("agent_nickname") or own
    scan = CodexScan(own, meta.get("agent_path"))
    for number, entry in numbered_lines(path):
        if not isinstance(entry, dict):
            raise MissingFieldError(f"{path}:{number}: the line is not a JSON object")
        payload = entry.get("payload")
        if not isinstance(payload, dict):
            continue
        where = f"{path}:{number}"
        at = required_time(entry, where)
        kind = entry.get("type")
        # Before the `turn_id` of any line is used as a key, the one of a record of tokens is read.
        record = codex_tokens(payload, own, where) if kind == "token_usage_record" else None
        turn = payload.get("turn_id")
        if turn:
            scan.first_seen.setdefault(turn, at)
            scan.last_seen[turn] = at
        if kind == "event_msg":
            scan.read_event(payload, turn, at)
        elif kind == "turn_context" and turn:
            scan.models[turn] = payload.get("model")
        elif kind == "response_item":
            scan.read_response_item(payload, at)
        elif record:
            scan.own_turns.add(record[0])
            scan.raw.append((at, record[0], record[1]))
    return codex_agent(scan, name, parent)


def codex_subagent_paths(home: Path, root: str, since: datetime | None) -> list[tuple[Path, str]]:
    """Every rollout under `home/sessions` descending from `root`, with its parent's id. Where
    `since`, the time of the orchestrator's first turn, is None, no rollout is left out by its
    time."""
    parents: dict[str, tuple[Path, str]] = {}
    floor = None if since is None else since.timestamp() - 1
    for path in (home / "sessions").rglob("rollout-*.jsonl"):
        if floor is not None and path.stat().st_mtime < floor:
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
    since = min((start for start, _ in orchestrator.turns), default=None)
    subagents = [
        read_codex_agent(p, parent)
        for p, parent in codex_subagent_paths(codex_home, orchestrator.key, since)
    ]
    return Session("Codex", orchestrator.key, path, orchestrator, subagents)


# Claude Code


def text_of(value: object) -> str:
    """`value` where it is a text, else the empty text: what a crafted transcript puts in a field
    of another kind is no name, no identifier and no model."""
    return value if isinstance(value, str) else ""


COUNT_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)
# The cache writes of each lifetime, in `message.usage.cache_creation`.
LIFETIME_FIELDS = ("ephemeral_5m_input_tokens", "ephemeral_1h_input_tokens")


def is_text(entry: dict) -> bool:
    """A user line holding text rather than a tool's result."""
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    # A content that is neither a text nor a list holds no text.
    return (
        isinstance(content, list)
        and bool(content)
        and isinstance(content[0], dict)
        and content[0].get("type") == "text"
    )


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
    return "\n".join(
        block["text"]
        for block in content_blocks(entry)
        if block.get("type") == "text" and isinstance(block.get("text"), str)
    )


def claude_counts(message: dict, where: str) -> dict[str, int]:
    """The token counts of a response of Claude Code, `where` naming its file and line: the four
    counts of `message.usage` and the two cache writes of `message.usage.cache_creation`, each
    needed; one that is missing, or is no whole number, ends the reading."""
    usage = required(message, "usage", "message.usage", where)
    counts = {
        key: required_count(usage, key, f"message.usage.{key}", where) for key in COUNT_FIELDS
    }
    creation = required(usage, "cache_creation", "message.usage.cache_creation", where)
    for lifetime in LIFETIME_FIELDS:
        counts[lifetime] = required_count(
            creation, lifetime, f"message.usage.cache_creation.{lifetime}", where
        )
    return counts


def claude_usage(counts: dict[str, int]) -> Usage:
    """The tokens of a response from its counts: input holds the cache writes and the part read
    from a cache."""
    return Usage(
        counts["input_tokens"]
        + counts["cache_creation_input_tokens"]
        + counts["cache_read_input_tokens"],
        counts["cache_read_input_tokens"],
        counts["output_tokens"],
        write_5m=counts["ephemeral_5m_input_tokens"],
        write_1h=counts["ephemeral_1h_input_tokens"],
    )


def read_claude_agent(path: Path, key: str, name: str, parent: str | None) -> Agent:
    responses: dict[str, tuple[datetime, dict[str, int], str | None]] = {}
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
    for number, entry in numbered_lines(path):
        if not isinstance(entry, dict) or "timestamp" not in entry:
            continue
        if entry.get("type") not in ("user", "assistant"):
            continue
        where = f"{path}:{number}"
        at = required_time(entry, where)
        required(required(entry, "message", "message", where), "content", "message.content", where)
        if entry.get("type") == "user":
            tail.clear()
            for block in content_blocks(entry):
                if block.get("type") == "tool_result" and text_of(block.get("tool_use_id")):
                    results.setdefault(block["tool_use_id"], at)
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
        else:
            message = entry["message"]
            model = message.get("model")
            if model == "<synthetic>":
                continue
            counts = claude_counts(message, where)
            activity.append(at)
            # Claude Code writes one response over several lines, which share its id.
            ident = text_of(message.get("id")) or text_of(entry.get("uuid")) or None
            if ident != tail_response:
                tail.clear()
                tail_response = ident
            for block in content_blocks(entry):
                kind = text_of(block.get("type"))
                call_name = text_of(block.get("name"))
                if kind == "tool_use" and call_name in CLAUDE_SUBAGENT_CALLS:
                    continue
                if kind == "tool_use" and text_of(block.get("id")):
                    started_calls.setdefault(block["id"], (at, call_name or kind))
                    tail.add(block["id"])
                elif kind == "tool_use" or kind.endswith("_tool_use"):
                    unrecognised.append(Call(at, None, call_name or kind, known=False))
            if message.get("stop_reason"):
                answered = message["stop_reason"] == "end_turn"
            kept = responses.get(ident)
            if kept is None or counts["output_tokens"] >= kept[1]["output_tokens"]:
                responses[ident] = (at, counts, text_of(model) or None)
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
    split = sum(
        1
        for _, usage, _ in responses.values()
        if usage["ephemeral_5m_input_tokens"] + usage["ephemeral_1h_input_tokens"]
        != usage["cache_creation_input_tokens"]
    )
    if split:
        agent.notes.append(
            f"{split} response(s) whose cache writes by lifetime do not add up to "
            f"cache_creation_input_tokens in {path}"
        )
    for at, counts, model in responses.values():
        agent.records.append(Record(at, claude_usage(counts), model))
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
                transcript, agent_id, name, meta.get("parentAgentId") or session_id
            )
            subagent.notes.extend(notes)
            subagents.append(subagent)
    known = {agent.key for agent in subagents}
    for agent in subagents:
        if agent.parent not in known:
            agent.parent = session_id
    return Session("Claude Code", session_id, path, orchestrator, subagents)


def read_session(path: Path, codex_home: Path) -> Session:
    entry = first_line(path)
    if not isinstance(entry, dict):
        raise CycleStagesError(f"{path} is neither a Codex rollout nor a Claude Code transcript")
    if entry.get("type") == "session_meta":
        meta = entry.get("payload") or {}
        if meta.get("parent_thread_id"):
            raise CycleStagesError(f"{path} is a subagent's rollout, not an orchestrator's")
        return read_codex_session(path, codex_home)
    if "sessionId" in entry or "type" in entry:
        return read_claude_session(path)
    raise CycleStagesError(f"{path} is neither a Codex rollout nor a Claude Code transcript")
