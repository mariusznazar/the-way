"""Crafted inputs at the trust boundary of plan_check.py and plan_state.py (review working copy).

Run: python -B crafted.py <the-way checkout> <output file> <scratch directory>
"""

import os
import subprocess
import sys

root, out_path, scratch = sys.argv[1], sys.argv[2], sys.argv[3]
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(root, "project-level"))
import test_plan_check as t  # noqa: E402

CLOSED = "Status: closed 2026-11-19"
HANDED = "Status: handed over 2026-10-06"
DROPPED = "dropped — approved by human"
lines = []


def show(label, text, definition=t.DEFINITION):
    found = t.findings(text, definition)
    lines.append("%s -> %s" % (label, [(f.condition, f.line) for f in found] or "nothing"))
    for f in found:
        lines.append("      " + str(f))


def closed(tasks=None, status=CLOSED, **kw):
    return t.plan(status=status, tasks=t.ALL_FINISHED if tasks is None else tasks, **kw)


lines.append("== plan_check.check: the Status line")
show("closed, every row final", closed())
show("the same, CRLF", closed().replace("\n", "\r\n"), t.DEFINITION)
in_cycle = t.changed(t.ALL_FINISHED, 1, "State", "in cycle")
show("closed, row 1 in cycle, CRLF", closed(in_cycle).replace("\n", "\r\n"))
for label, status in (
    ("trailing NBSP", CLOSED + " "),
    ("trailing U+2028", CLOSED + " "),
    ("trailing form feed", CLOSED + "\x0c"),
    ("trailing U+001F", CLOSED + "\x1f"),
    ("trailing zero-width space", CLOSED + "​"),
    ("fullwidth digits", "Status: closed ２０２６-11-19"),
    ("Arabic-Indic digits", "Status: closed ٢٠٢٦-١١-١٩"),
    ("double space", "Status: closed  2026-11-19"),
    ("tab after closed", "Status: closed\t2026-11-19"),
    ("two spaces after colon", "Status:  closed 2026-11-19"),
    ("lower-case label", "status: closed 2026-11-19"),
    ("leading space", " Status: closed 2026-11-19"),
    ("leading BOM on the line", "﻿Status: closed 2026-11-19"),
    ("date with Z", "Status: closed 2026-11-19Z"),
    ("year 0000", "Status: closed 0000-01-01"),
    ("year 9999", "Status: closed 9999-12-31"),
    ("29 February of 2026", "Status: closed 2026-02-29"),
    ("month 13", "Status: closed 2026-13-01"),
    ("non-hyphen dashes", "Status: closed 2026–11–19"),
    ("closed then bare CR then handed over", CLOSED + "\r" + HANDED),
    ("closed twice", CLOSED + "\n" + CLOSED),
    ("draft then closed", "Status: draft\n" + CLOSED),
    ("closed then draft", CLOSED + "\nStatus: draft"),
    ("off-form line then closed", "Status:draft\n" + CLOSED),
    ("closed in an HTML comment, then handed over", "<!-- " + CLOSED + " -->\n" + HANDED),
    ("closed in a code fence, then handed over", "```\n" + CLOSED + "\n```\n" + HANDED),
):
    show(label + " (row 1 in cycle)", closed(in_cycle, status))

lines.append("== plan_check.check: a Status line below the first section only")
text = closed(in_cycle, status="")
text = text.replace("## Tasks\n", "## Tasks\n\n" + CLOSED + "\n", 1)
show("closed line under ## Tasks, row 1 in cycle", text)

lines.append("== plan_check.check: the rows of a closed plan")
dropped_1 = t.changed(t.ALL_FINISHED, 1, "State", DROPPED)
show("row 2 delivered in dropped task 1", closed(dropped_1))
show("the same in a handed-over plan", closed(dropped_1, HANDED))
chain = t.changed(dropped_1, 3, "State", "done — goal delivered in task 2")
show("3 delivered in 2, 2 delivered in 1, 1 dropped", closed(chain))
mutual = t.changed(t.ALL_FINISHED, 2, "State", "done — goal delivered in task 3")
mutual = t.changed(mutual, 3, "State", "done — goal delivered in task 2")
show("2 delivered in 3 and 3 delivered in 2 (no task made either)", closed(mutual))
every = [row[:6] + ("done — goal delivered in task %d" % n,) + row[7:] for row, n in zip(t.TASKS, (2, 3, 1))]
show("every row delivered in another, in a ring", closed(every))
all_dropped = [row[:6] + (DROPPED,) + row[7:] for row in t.TASKS]
show("every row dropped", closed(all_dropped))
for label, state in (
    ("state Done", "Done"),
    ("state with hyphen", "dropped - approved by human"),
    ("state done with NBSP after", "done "),
    ("delivered in task with fullwidth digit", "done — goal delivered in task １"),
    ("delivered in task 01", "done — goal delivered in task 01"),
    ("delivered in itself", "done — goal delivered in task 2"),
    ("delivered in task 9", "done — goal delivered in task 9"),
    ("state empty", ""),
    ("state done twice", "done done"),
    ("state done with an escaped pipe", "done \\| in cycle"),
):
    show(label + " (row 2)", closed(t.changed(t.ALL_FINISHED, 2, "State", state)))
twins = list(t.ALL_FINISHED) + [("1",) + t.ALL_FINISHED[2][1:2] + t.ALL_FINISHED[2][2:]]
twins = t.changed(twins, 4, "Task", "twin")
show("a second row numbered 1 that is dropped, row 2 delivered in task 1", closed(twins))
show("closed, a tasks table with no row", closed(()))
log = (
    "- 2026-10-05 — written from the definition at fingerprint %s\n"
    "- 2026-11-19 — project closed — the project closes with its tasks done or withdrawn\n"
    "  - tasks: 1 done, 1 done — goal delivered in another task, 1 withdrawn\n"
    "  - withdrawn: task 3 `player-accounts` — dropped for good: no accounts in this version\n"
    "  - not delivered: item 2 of In scope — zapis postępu gracza\n"
    "  - not delivered: item 3 of In scope — konta graczy\n"
    '  - projected entries not written by a withdrawn task: `%s` (task 3) — absent from the foundation at commit 0123abc\n'
    % (t.FINGERPRINT, t.DECISION_HEADING)
)
show("closed, with a closing item of the form closure.md gives", closed(bodies={"Change log": log.rstrip("\n")}))

lines.append("== plan_state.py as a process")
os.makedirs(scratch, exist_ok=True)
definition_path = os.path.join(scratch, "definition.md")
plan_path = os.path.join(scratch, "plan.md")
script = os.path.join(root, "project-level", "plan_state.py")


def state(label, text, repository, newline="\n", bom=False):
    with open(definition_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(t.DEFINITION.replace("\n", newline))
    with open(plan_path, "w", encoding="utf-8-sig" if bom else "utf-8", newline="") as handle:
        handle.write(text.replace("\n", newline))
    run = subprocess.run(
        [sys.executable, "-B", script, plan_path, repository],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    lines.append("%s -> exit %d" % (label, run.returncode))
    for line in (run.stdout + run.stderr).splitlines():
        for place in (os.path.normpath(scratch), scratch):
            line = line.replace(place, "<scratch>")
        lines.append("      " + line)


missing = os.path.join(scratch, "no-such-repository")
state("closed, every row final, repository that does not exist", closed(), missing)
state("handed over, the same rows, repository that does not exist", closed(status=HANDED), missing)
state("closed, CRLF and BOM", closed(), missing, newline="\r\n", bom=True)
state("closed with trailing NBSP", closed(status=CLOSED + " "), missing)
state("closed, row 1 in cycle", closed(in_cycle), missing)
state("closed, row 2 delivered in dropped task 1", closed(dropped_1), missing)
state("closed, 2 and 3 delivered in each other", closed(mutual), missing)
state("closed twice", closed(status=CLOSED + "\n" + CLOSED), missing)
state("closed then handed over", closed(status=CLOSED + "\n" + HANDED), missing)
state("handed over then closed", closed(status=HANDED + "\n" + CLOSED), missing)
state("closed 2026-02-30", closed(status="Status: closed 2026-02-30"), missing)
state("closed with fullwidth digits", closed(status="Status: closed ２０２６-11-19"), missing)
state("closed line under ## Tasks only", text, missing)
changed_definition = closed(fingerprint=t.OTHER_FINGERPRINT)
state("closed, fingerprint other than the definition's", changed_definition, missing)

with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
    handle.write("\n".join(lines) + "\n")
print("written", len(lines), "lines")
