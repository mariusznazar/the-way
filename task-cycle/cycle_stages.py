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
for the human is left out. That wait depends on when the human reads, not on the process. A token
count belongs to the stage running when its entry is written: the subagent's to the turn it falls
in, the orchestrator's to the subagent turn then running or to the orchestrator's stretch; while
several subagent turns run at once, the orchestrator's tokens go to a row of their own naming them,
rather than being split by a guess.

Tokens are counted as each tool reports them per model response: input with the cache writes and
the part read from a cache, and output with reasoning. The cache writes of each lifetime, five
minutes and one hour, are written apart in the detailed section, as the columns *Cache write (5
minutes)* and *Cache write (1 hour)*; they are parts of input, and a Codex record gives none, so its
columns read 0. Claude Code writes one response over several lines that repeat its usage; each
response counts once.

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
subagent with no turn or no token usage, a response naming no model, a response whose cache writes
by lifetime do not add up to its `cache_creation_input_tokens`, a Codex subagent turn with no
`task_complete`, a Claude Code subagent with no `.meta.json`, a call with no result or of an
unrecognised type — since a line the reader no longer recognises is skipped and its tokens and
waits go uncounted.

A Claude Code transcript is untrusted input, and each field the reading needs has to be there. Of
every `user` or `assistant` line that has a `timestamp` it needs the `timestamp`, as a time, and
`message` and `message.content`; of every `assistant` line whose model is not `<synthetic>`, also
`message.usage` with `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` and
`output_tokens`, and `cache_creation` with `ephemeral_5m_input_tokens` and
`ephemeral_1h_input_tokens`, each a non-negative whole number of at most 15 digits. A `null` is a
missing field. A field that is missing, or a count that is no whole number, ends the run with a
message that names the transcript, the line and the field. Read with a fallback, and no error where absent: a line with no
`timestamp`, which is skipped before its type is looked at, a line that is no JSON object, `type`,
`isMeta`,
`message.model` (absent, `null` or no text it counts under the model `unknown`, with the warning),
`message.id` (the line's `uuid` stands for it), `message.stop_reason`, and of a content block its
`id`, `name`, `tool_use_id` and `text`.

A Codex rollout is untrusted input too, and each field the reading needs has to be there. Of the
first line, its `session_meta`, it needs `payload.id`, the session's id, as a text that is not
empty; of every line whose `payload` is an object, its `timestamp`, as a time; of every
`token_usage_record`, `payload.thread_id` as a text that is not empty, and of one whose
`thread_id` is the rollout's own id, the agent's own, also `payload.turn_id` as such a text and
`payload.usage` with `input_tokens`, `cached_input_tokens` and `output_tokens`, each a non-negative
whole number of at most 15 digits, as for a response of Claude Code. A `null` is a missing field. A
field that is missing, or a count that is no whole number, ends the run with a message that names
the rollout, the line and the field. A record of another thread, which a forked rollout repeats
from its parent's history, is no record of the agent and is not read further. The reading of the
other fields of a rollout checks nothing, nor does the reading of `agent-<id>.meta.json`: a line
whose `payload` is no object is skipped, and the other fields of a line are read with a fallback.
The text of a transcript reaches the report only through `cell`; a count in it is a whole number
read here.

Exit code: 0 on success, warnings included; 2 with `Error: <message>` on stderr and nothing written
for a field of a Claude Code transcript or of a Codex rollout that is missing or no whole number
or no time or no text; 1 with `Error: <message>` on stderr for the rest, such as a session that
cannot be found or read and a line that is not JSON.

Standard library only.
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from stage_transcripts import (
    Agent,
    Call,
    CycleStagesError,
    MissingFieldError,
    Session,
    Usage,
    read_session,
)


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
    raise CycleStagesError(
        f"session {name!r} matches several transcripts: " + ", ".join(str(p) for p in found)
    )


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


def overlap(
    intervals: list[tuple[datetime, datetime]], start: datetime | None, end: datetime | None
) -> timedelta:
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
                    Row(
                        start,
                        agent.name + (f" — turn {n}" if count > 1 else ""),
                        end - start,
                        window=(start, end),
                        named=named,
                        usage_read=bool(agent.records),
                    )
                    for n, ((start, end), named) in enumerate(zip(agent.turns, agent.turn_files), 1)
                ]
    owned = sorted(
        (
            (record, top_level(agent, by_key, roots).key)
            for session in sessions
            for agent in session.subagents
            for record in agent.records
        ),
        key=lambda pair: pair[0].at,
    )
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
        stretches.append(
            Row(
                stretch_start(start, end, active),
                "orchestrator",
                overlap(active, start, end),
                window=(start, end),
                usage_read=orchestrator_read,
            )
        )
    parallel: dict[frozenset[int], Row] = {}

    def orchestrator_row(at: datetime) -> Row:
        """The row the orchestrator's work at a moment is counted in: the stage running then, the
        row of the stages running together, or the orchestrator's stretch between stages."""
        running = [i for i, row in enumerate(stage_rows) if row.window[0] <= at <= row.window[1]]
        if len(running) == 1:
            return stage_rows[running[0]]
        if running:
            group = frozenset(running)
            if group not in parallel:
                names = ", ".join(stage_rows[i].name for i in sorted(running))
                parallel[group] = Row(
                    at,
                    f"orchestrator while in parallel: {names}",
                    None,
                    usage_read=orchestrator_read,
                )
            return parallel[group]
        return next(
            r
            for r in stretches
            if (r.window[0] is None or r.window[0] < at)
            and (r.window[1] is None or at < r.window[1])
        )

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


def stretch_start(
    start: datetime | None, end: datetime | None, active: list[tuple[datetime, datetime]]
) -> datetime:
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
    # A lone surrogate, which JSON allows in a string, cannot be written as UTF-8.
    return " ".join(text.split()).encode("utf-8", errors="replace").decode("utf-8")


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
        lines.append(
            f"- {session.tool} session `{session.id}`: {len(session.subagents)} "
            f"subagents — `{session.path.name}`"
        )
    lines += ["", "Warnings:" if warnings else "Warnings: none."]
    lines += [f"- {one_line(warning)}" for warning in warnings]
    lines += [
        "",
        "A stage is one turn of a subagent the orchestrator started, from its prompt to its "
        "answer, or a stretch of the orchestrator's own work between such turns. Durations are "
        "h:mm:ss; an orchestrator stretch counts only the time inside the orchestrator's turns, "
        "never the wait for the human. Tokens are input, which includes the cache writes and the "
        "part read from a cache, plus output, which includes reasoning.",
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
            f"| {number(both.total)} | {number(both.cached)} | {number(both.output)} |"
        )
    by_model: dict[str, Usage] = {}
    for session in sessions:
        for agent in [session.orchestrator, *session.subagents]:
            for record in agent.records:
                by_model.setdefault(record.model or "unknown", Usage()).add(record.usage)
    active = merge(
        [turn for session in sessions for turn in session.orchestrator.turns]
        + [row.window for row in rows if row.duration is not None and row.name != "orchestrator"]
    )
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
        f"- Working time, orchestrator turns and subagent turns joined: {duration_text(working)}",
        *waiting_lines,
        f"- Tokens in all: {number(totals.total)} — cached input {number(totals.cached)}, "
        f"output {number(totals.output)}",
        "",
        "| Model | Total tokens | Input | Cached input | Output |",
        "|---|---|---|---|---|",
    ]
    for model, usage in sorted(by_model.items(), key=lambda item: -item[1].total):
        lines.append(
            f"| {cell(model)} | {number(usage.total)} | {number(usage.input)} "
            f"| {number(usage.cached)} | {number(usage.output)} |"
        )
    lines += [
        "",
        "## Stages: start, waiting for tools and tokens by model",
        "",
        "Times are UTC. Each stage's waiting for tools is the time of its tool calls, from each "
        "call to its result; `unknown` marks a stage with a call whose result was not read or "
        "whose type is not recognised. Input includes the cache writes and the part read from a "
        "cache. *Cache write (5 minutes)* and *Cache write (1 hour)* give the cache writes of each "
        "lifetime, which are parts of *Input*; a Codex record gives none, so its rows show 0. The "
        "model `—` marks a stage with no token usage, and `unknown` with zero counts one whose "
        "transcript holds no token usage at all, so that its usage was not read. *Files named* "
        "lists the files of the cycle's `reports/` that the message starting a subagent turn "
        "names — its prompt, or the message that resumes it — each once; it is empty where that "
        "message names none and for the orchestrator's rows, and `unknown` where the message "
        "cannot be read.",
        "",
        "| # | Stage | Start | Waiting for tools | Model | Input | Cached input | Output "
        "| Files named | Cache write (5 minutes) | Cache write (1 hour) |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for index, row in enumerate(rows, 1):
        models = sorted(row.by_model.items(), key=lambda item: -item[1].total) or [
            ("—" if row.usage_read else "unknown", Usage())
        ]
        named = "unknown" if row.named is None else cell(", ".join(row.named))
        for model, usage in models:
            lines.append(
                f"| {index} | {cell(row.name)} | {clock_text(row.start)} "
                f"| {wait_text(row.calls)} | {cell(model)} | {number(usage.input)} "
                f"| {number(usage.cached)} | {number(usage.output)} | {named} "
                f"| {number(usage.write_5m)} | {number(usage.write_1h)} |"
            )
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
        raise CycleStagesError(
            "name a session; neither " + " nor ".join(SESSION_VARIABLES) + " is set"
        )
    # A tool started from the other's terminal inherits its variable.
    raise CycleStagesError("name a session; both " + " and ".join(SESSION_VARIABLES) + " are set")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("sessions", nargs="*", metavar="SESSION")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--codex-home", type=Path, default=default_home("CODEX_HOME", ".codex"))
    parser.add_argument(
        "--claude-home", type=Path, default=default_home("CLAUDE_CONFIG_DIR", ".claude")
    )
    args = parser.parse_args(argv)
    try:
        names = args.sessions or [current_session()]
        paths = dict.fromkeys(
            resolve(name, args.codex_home, args.claude_home).resolve() for name in names
        )
        sessions = [read_session(path, args.codex_home) for path in paths]
        warnings = find_warnings(sessions)
        text = report(sessions, build_rows(sessions), warnings)
    except MissingFieldError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2
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
