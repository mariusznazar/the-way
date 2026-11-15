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
already found, as its parent_thread_id. Each one is an agent of its own. A rollout last modified
before the orchestrator's first call is not read; every other rollout under the home has its first
line read, and one that cannot be read ends the run. A second rollout with an id already found is
left out, and a `Warning:` line on stderr names it.

A call of a Claude Code agent is one model response. Claude Code writes a response over several lines
that share its id; each id counts once, from the line with the most output tokens. A response whose
model is `<synthetic>` is no call.

A call of a Codex agent is one token usage record of the agent's own thread. Its context is its
input tokens, which already hold the part read from the cache. Codex's record has no cache write by
lifetime and its write field is a constant 0, which measures nothing, so the cache figures of a
Codex agent are unknown, never zero.

The decision log and its index in an agent's context. For each agent the table of agents gives, in
its last four columns, how many bytes of the product's decision log and of the index of decisions
(written by `elements/common/decision_index.py`) entered its context, and how many times each
entered it. A read is a tool call paired with its result:

- Claude Code: a block `tool_use` of an assistant line, paired by its `id` with the block
  `tool_result` of a later user line that names it in `tool_use_id`. Lines of another type, such as
  a replay of a request, are not read. Each `tool_use` id counts once: a repeated id is the same
  call, and a second result for it, a result whose id no `tool_use` of the agent names and a result
  that stands before its call are not counted and are no error.
- Codex: a record `response_item` whose payload is a `function_call` (its `arguments`, a JSON text)
  or a `custom_tool_call` (its `input`, a text), paired by `call_id` with the payload
  `function_call_output` or `custom_tool_call_output` of a later record, the same rules holding. The
  form was read from rollouts under the Codex home.

It is a read of the log where a text value of the call's input, at any depth (a file path, a search
path, a shell command), names a path that ends with `foundations/decisions.md`, each run of
backslashes and slashes taken as one slash (a path in the source text of a Codex custom tool call
has its backslashes doubled). The path is whole: no character of a name, `.` or `-` stands before
it, and neither a character of a name or `-`, nor a `.` with a character of a name after it, follows
it (`foundations/decisions.md.bak` and `myfoundations/decisions.md` are other files). It is a read
of the index where the text of the result holds a line that begins with `# decision_index.py:`, the
start of both title lines of the index (the index of decisions and the list of sections), which the
number that a Read tool puts before a line may precede. The bytes are the UTF-8 bytes of the
result's text as the transcript holds it: a result that is a text, or the `text` blocks of a result
that is a list, joined with nothing between them (Codex: the blocks of type `input_text`); nothing
else is counted, and a lone surrogate in the text counts as the three bytes it takes.

What stays approximate:

- A search or a command over a directory that holds the log without naming it is not counted.
- A command that names the log counts its whole output, other files' lines included; a call of any
  tool that names the log in its input counts the text its result holds, whether the call read the
  log or not (an edit of it, an agent told to read it).
- A result that the tool cut, or kept in a file, counts what the transcript holds; a result that
  reports an error counts the text of the error.
- A copy of the log under another path is not counted; the-way's own log in a product's `.the-way/`
  is counted, since its path ends with `foundations/decisions.md`. Passages of the log in a handoff,
  and a part of the index read without its title line, are not counted.
- A text that quotes a title line of the index at the start of a line counts as a read of the index.
- A forked Codex rollout that repeated its parent's tool records would count them again; the
  rollouts read had no call id in common with their parent's.

The transcript is untrusted input. Each field the reading needs has to be there, or the run ends with
exit code 2 and a message that names the file, the line and the field: of a tool call its `id`,
`name` and `input` (Codex: `call_id`, `name` and `arguments` or `input`), of a result its
`tool_use_id` and `content` (Codex: `call_id` and `output`); of every assistant or user line its
`message` and `message.content` (Codex: of every `response_item` its `payload`); of a text block of a
result its `text`. A `null` is a missing field. A line or a block that is no tool call or result, a
content that is no string or list, a block that is no object and a result that is no text are not
counted and are no error. The `type` that tells one kind of block or record from another is not
checked: one that lacks it is a kind the reading does not know. Nothing of a transcript reaches the
file but through `cell`: the figures of the log and the index are whole numbers made here.

The file is Markdown, written to PATH or printed. Exit code: 0 when it is written; 2 with
`Error: <message>` on stderr and nothing written otherwise, for a session that cannot be found or
read, a line that is not JSON or too large to read into memory, a needed field that is missing or no
whole number, and a rollout of a subagent named as a session. Arguments of a Codex function call
too large to parse are searched as their text alone.

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from dataclasses import field as dataclass_field
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
SEPARATORS = re.compile("[" + chr(92) * 2 + "/]+")  # the class `[\\/]`: a backslash or a slash
LOG_PATH = re.compile(r"(?<![\w.-])foundations/decisions\.md(?![\w-]|\.\w)")
INDEX_TITLE = re.compile(r"^(?:[ \t]*\d+[\t\u2192])?# decision_index\.py:", re.MULTILINE)
CLAUDE_TEXT_BLOCKS = frozenset({"text"})
CODEX_TEXT_BLOCKS = frozenset({"input_text"})
CODEX_CALLS = {"function_call": "arguments", "custom_tool_call": "input"}
CODEX_OUTPUTS = frozenset({"function_call_output", "custom_tool_call_output"})


@dataclass(frozen=True)
class Call:
    at: datetime
    index: int
    context: int
    # The cache figures of the call; 0 for a Codex call, whose record gives none. That they are
    # unknown is held once, in `Agent.cache_known`, and no sum or rewrite is made without it.
    read: int
    write: int
    write_5m: int
    write_1h: int


@dataclass
class Reads:
    """The bytes of the decision log and of the index of decisions that entered an agent's context,
    and how many times each entered it."""
    log_bytes: int = 0
    log_reads: int = 0
    index_bytes: int = 0
    index_reads: int = 0


@dataclass
class Agent:
    name: str
    orchestrator: bool
    calls: list[Call]
    tool: str = CLAUDE
    reads: Reads = dataclass_field(default_factory=Reads)

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
    """The time of a line as an aware time: a naive one is taken as UTC, another offset is kept.
    A missing or unreadable time ends the reading."""
    value = member(entry, "timestamp", "timestamp", where)
    if not isinstance(value, str):
        raise MeasuresError(f"{where}: field timestamp is not a time")
    try:
        at = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise MeasuresError(f"{where}: field timestamp is not a time") from error
    return at if at.tzinfo else at.replace(tzinfo=timezone.utc)


def line_object(line: str, where: str) -> dict | None:
    """The object of one line of a JSON Lines file; None for a blank line. A line that is not JSON,
    or not an object, ends the reading with `where` named."""
    if not line.strip():
        return None
    try:
        entry = json.loads(line)
    except (ValueError, RecursionError) as error:
        raise MeasuresError(f"{where}: not JSON: {error}") from error
    if not isinstance(entry, dict):
        raise MeasuresError(f"{where}: not a JSON object")
    return entry


def json_lines(path: Path) -> Iterator[tuple[int, dict]]:
    """Each non-blank line of a JSON Lines file, as its number and its object. A line that is not
    JSON, not an object or too large to read into memory ends the reading with the file and the
    line named."""
    reading = 1  # the number of the line being read or parsed
    try:
        with path.open(encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                reading = number
                entry = line_object(line, f"{path}:{number}")
                reading = number + 1
                if entry is not None:
                    yield number, entry
    except MemoryError as error:
        raise MeasuresError(f"{path}:{reading}: the line is too large to read into memory") \
            from error
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


def text_values(value: object) -> Iterator[str]:
    """Every string among the values of a JSON value at any depth, found without recursion, so that
    a value nested as deeply as a line can be read ends no run."""
    stack = [value]
    while stack:
        item = stack.pop()
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            stack.extend(item.values())
        elif isinstance(item, list):
            stack.extend(item)


def names_log(texts: Iterable[str]) -> bool:
    """Whether a text names the decision log: a path that ends with `foundations/decisions.md`, with
    each run of backslashes and slashes taken as one slash, since a path in source text, such as the
    input of a Codex custom tool call, is written with its backslashes doubled."""
    return any(LOG_PATH.search(SEPARATORS.sub("/", text)) for text in texts)


def result_text(content: object, kinds: frozenset[str], label: str, where: str) -> str | None:
    """The text of a result: a string as it is, a list as the `text` of its blocks of the given kinds
    joined with nothing between them; None for any other content. A block of those kinds that lacks
    its `text` ends the reading, naming `label[index].text`."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for index, block in enumerate(content):
            if (isinstance(block, dict) and isinstance(block.get("type"), str)
                    and block["type"] in kinds):
                text = member(block, "text", f"{label}[{index}].text", where)
                if isinstance(text, str):
                    parts.append(text)
        return "".join(parts)
    return None


class ReadCounter:
    """Pairs the tool calls of one agent with their results and counts the reads of the log and of
    the index. Each call id counts once."""

    def __init__(self) -> None:
        self.reads = Reads()
        self.pending: dict[str, bool] = {}  # call id -> whether the call named the log
        self.settled: set[str] = set()

    def call(self, ident: str, named_log: bool) -> None:
        if ident not in self.settled:
            self.pending[ident] = self.pending.get(ident, False) or named_log

    def result(self, ident: str, text: str | None) -> None:
        named_log = self.pending.pop(ident, None)
        if named_log is None:
            return
        self.settled.add(ident)
        if text is None:
            return
        # A lone surrogate, which JSON allows in a string, counts as the three bytes it takes.
        size = len(text.encode("utf-8", errors="surrogatepass"))
        if named_log:
            self.reads.log_bytes += size
            self.reads.log_reads += 1
        if INDEX_TITLE.search(text):
            self.reads.index_bytes += size
            self.reads.index_reads += 1


def read_claude_blocks(entry: dict, where: str, counter: ReadCounter) -> None:
    """The tool calls of an assistant line and the results of a user line. Each field they need is
    read: a missing one ends the reading, the `message` and the `message.content` of the line
    included. A content that is no list, and anything that is no tool block, is not counted."""
    kind = entry.get("type")
    if kind not in ("assistant", "user"):
        return
    message = member(entry, "message", "message", where)
    content = member(message, "content", "message.content", where)
    if not isinstance(content, list):
        return
    for index, block in enumerate(content):
        if not isinstance(block, dict):
            continue
        label = f"message.content[{index}]"
        if kind == "assistant" and block.get("type") == "tool_use":
            ident = identifier(block, "id", f"{label}.id", where)
            identifier(block, "name", f"{label}.name", where)
            tool_input = member(block, "input", f"{label}.input", where)
            counter.call(ident, names_log(text_values(tool_input)))
        elif kind == "user" and block.get("type") == "tool_result":
            ident = identifier(block, "tool_use_id", f"{label}.tool_use_id", where)
            result = member(block, "content", f"{label}.content", where)
            counter.result(ident, result_text(result, CLAUDE_TEXT_BLOCKS, f"{label}.content",
                                              where))


def read_claude_agent(path: Path) -> tuple[list[Call], Reads]:
    """The calls of the Claude Code agent whose transcript this is, in the order of their time, and
    what it read of the decision log and of the index."""
    chosen: dict[str, tuple[int, Call]] = {}
    counter = ReadCounter()
    for number, entry in json_lines(path):
        where = f"{path}:{number}"
        if entry.get("type") != "assistant":
            read_claude_blocks(entry, where, counter)
            continue
        message = entry.get("message")
        if isinstance(message, dict) and message.get("model") == SYNTHETIC_MODEL:
            continue
        ident, output, call = read_response(entry, where, number)
        read_claude_blocks(entry, where, counter)
        kept = chosen.get(ident)
        if kept is None or output >= kept[0]:
            chosen[ident] = (output, call)
    calls = [call for _, call in chosen.values()]
    calls.sort(key=lambda call: (call.at, call.index))
    return calls, counter.reads


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
        except (OSError, UnicodeDecodeError, ValueError, RecursionError, MemoryError) as error:
            raise MeasuresError(f"cannot read {meta_path}: {error}") from error
    if not isinstance(meta, dict):
        meta = {}
    description = meta.get("description") or agent_id
    kind = meta.get("agentType")
    return f"{description} ({kind})" if kind else str(description)


def read_claude_session(path: Path) -> list[Agent]:
    """The orchestrator of a Claude Code session and each subagent of its folder, each as an agent."""
    session_id = path.stem
    calls, reads = read_claude_agent(path)
    agents = [Agent(f"orchestrator {session_id}", True, calls, reads=reads)]
    folder = path.with_suffix("") / "subagents"
    if folder.is_dir():
        for transcript in sorted(folder.glob("agent-*.jsonl")):
            agent_id = transcript.stem.removeprefix("agent-")
            calls, reads = read_claude_agent(transcript)
            agents.append(Agent(read_subagent_name(transcript, agent_id), False, calls,
                                reads=reads))
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


def read_codex_record(entry: dict, where: str, counter: ReadCounter) -> None:
    """A tool call or the output of one, from a record `response_item`. Each field it needs is read:
    a missing one ends the reading, the `payload` of the record included. A payload that is no object
    or of another kind is not counted."""
    payload = member(entry, "payload", "payload", where)
    kind = payload.get("type") if isinstance(payload, dict) else None
    if not isinstance(kind, str):
        return
    if kind in CODEX_CALLS:
        key = CODEX_CALLS[kind]
        ident = identifier(payload, "call_id", "payload.call_id", where)
        identifier(payload, "name", "payload.name", where)
        arguments = member(payload, key, f"payload.{key}", where)
        texts = list(text_values(arguments))
        if kind == "function_call" and isinstance(arguments, str):
            try:
                texts.extend(text_values(json.loads(arguments)))
            except (ValueError, RecursionError, MemoryError):
                pass  # not JSON, or too large to parse: the text itself was searched
        counter.call(ident, names_log(texts))
    elif kind in CODEX_OUTPUTS:
        ident = identifier(payload, "call_id", "payload.call_id", where)
        output = member(payload, "output", "payload.output", where)
        counter.result(ident, result_text(output, CODEX_TEXT_BLOCKS, "payload.output", where))


def read_codex_calls(path: Path, ident: str) -> tuple[list[Call], Reads]:
    """The calls of the agent whose thread is `ident`: the token usage records of that thread, in
    the order of their time, and what its tool calls read of the decision log and of the index. A
    forked subagent's rollout repeats its parent's token usage records, which are no calls of its
    own."""
    calls = []
    counter = ReadCounter()
    for number, entry in json_lines(path):
        where = f"{path}:{number}"
        if entry.get("type") == "response_item":
            read_codex_record(entry, where, counter)
            continue
        if entry.get("type") != "token_usage_record":
            continue
        payload = member(entry, "payload", "payload", where)
        if identifier(payload, "thread_id", "payload.thread_id", where) != ident:
            continue
        usage = member(payload, "usage", "payload.usage", where)
        input_tokens = whole(usage, "input_tokens", "payload.usage.input_tokens", where)
        calls.append(Call(at=read_time(entry, where), index=number, context=input_tokens,
                          read=0, write=0, write_5m=0, write_1h=0))
    calls.sort(key=lambda call: (call.at, call.index))
    return calls, counter.reads


def codex_subagents(home: Path, root: str,
                    since: datetime | None) -> list[tuple[Path, RolloutMeta]]:
    """Every rollout under `home/sessions` that descends from `root`, as its path and identity. A
    rollout descends from a rollout whose id its parent_thread_id names; the search goes level by
    level, each level in the order of the paths. A rollout last modified more than a second before
    `since`, the time of the orchestrator's first call, cannot be one of its subagents and is not
    read; every other rollout is, and an unreadable first line of one ends the reading. A second
    rollout with an id already found is left out, and a warning on stderr names it."""
    children: dict[str, list[tuple[Path, RolloutMeta]]] = {}
    sessions = home / "sessions"
    floor = None if since is None else since.timestamp() - 1
    if sessions.is_dir():
        for path in sorted(sessions.rglob("rollout-*.jsonl")):
            try:
                if floor is not None and path.stat().st_mtime < floor:
                    continue
            except OSError as error:
                raise MeasuresError(f"cannot read {path}: {error}") from error
            meta = rollout_meta(path)
            if meta is not None and meta.parent is not None:
                children.setdefault(meta.parent, []).append((path, meta))
    found: list[tuple[Path, RolloutMeta]] = []
    known = {root}
    queue = [root]
    while queue:
        for path, meta in children.get(queue.pop(0), []):
            if meta.ident in known:
                print(f"Warning: {path} has the id {meta.ident} of an agent already found; its "
                      "calls are not counted", file=sys.stderr)
                continue
            known.add(meta.ident)
            found.append((path, meta))
            queue.append(meta.ident)
    return found


def read_codex_session(path: Path, meta: RolloutMeta, codex_home: Path) -> list[Agent]:
    """The orchestrator of a Codex session and each subagent under it, each as an agent."""
    if meta.parent is not None:
        raise MeasuresError(f"{path} is a subagent's rollout, not an orchestrator's")
    calls, reads = read_codex_calls(path, meta.ident)
    agents = [Agent(f"orchestrator {meta.ident}", True, calls, CODEX, reads)]
    since = min((call.at for call in calls), default=None)
    for sub_path, sub in codex_subagents(codex_home, meta.ident, since):
        sub_calls, sub_reads = read_codex_calls(sub_path, sub.ident)
        agents.append(Agent(sub.name, False, sub_calls, CODEX, sub_reads))
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
    counts only above the floor, and not where the context fell by 30% or more. A collapse of the
    conversation drops part of the context and the cache is written anew after it though nothing
    expired, so counted as a rewrite it would make a change that adds collapses look like a
    worsening."""
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
    record has no cache write by lifetime and a write field that is a constant 0."""
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
        str(agent.reads.log_bytes),
        str(agent.reads.log_reads),
        str(agent.reads.index_bytes),
        str(agent.reads.index_reads),
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
        "| Cache written, 1 hour | Cache written again | Calls with a cache write again "
        "| Decision log bytes | Decision log reads | Decision index bytes | Decision index reads |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
