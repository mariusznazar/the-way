"""Recompute every fingerprint a relation of the decision log carries (foundation author's check).

Usage: python -B foundation_fingerprints.py <repository root> [--show WAY-NN ...] [--from NN]

Reads foundations/decisions.md (and foundations/invariants.md for *Derives from* links), computes
the fingerprint of the latest version's binding sentences of every decision with
relation-model/fingerprint.py, and compares it with every `derives from` / `narrows` relation of
every decision and every *Derives from* link of every invariant. Prints one line per relation of
the decisions numbered from --from on, and every stale relation anywhere. Exit 1 on a stale one.
"""

import importlib.util
import re
import sys
from pathlib import Path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main(argv):
    root = Path(argv[0])
    show = []
    start = None
    rest = argv[1:]
    while rest:
        if rest[0] == "--show":
            rest = rest[1:]
            while rest and not rest[0].startswith("--"):
                show.append(rest.pop(0))
        elif rest[0] == "--from":
            start = int(rest[1])
            rest = rest[2:]
        else:
            raise SystemExit("unknown argument %s" % rest[0])
    fp = load("fingerprint", root / "relation-model" / "fingerprint.py").fingerprint
    sys.path.insert(0, str(root / "elements" / "common"))
    guard = load("decisions_format_guard", root / "elements" / "decisions" / "format_guard.py")
    text = (root / "foundations" / "decisions.md").read_text(encoding="utf-8")
    prefix = guard.detect_prefix(text)
    entries = [e for e in guard.parse_log(text, prefix) if e.kind == "version"]
    latest = {}
    for entry in entries:
        if entry.number not in latest or entry.version > latest[entry.number].version:
            latest[entry.number] = entry
    current = {n: (fp(e.binding) if e.binding else None) for n, e in latest.items()}

    for name in show:
        number = int(name.split("-")[1])
        print("binding %s/%s fingerprint %s" % (name, latest[number].version, current.get(number)))

    stale = 0
    checked = 0
    for entry in entries:
        value = entry.fields.get("Relations", ["", 0])[0]
        if value in ("", "none"):
            continue
        for item in [i.strip() for i in value.split(" · ")]:
            match = re.fullmatch(r"(derives from|narrows) %s-(\d{2,})@([0-9a-f]+)" % prefix, item)
            if not match:
                print("UNREAD %s-%02d/%d: %s" % (prefix, entry.number, entry.version, item))
                stale += 1
                continue
            checked += 1
            target = int(match.group(2))
            want = current.get(target)
            ok = want == match.group(3)
            if not ok:
                stale += 1
            if not ok or (start is not None and entry.number >= start):
                print("%s %s-%02d/%d %s %s-%02d@%s (current %s)" % (
                    "ok   " if ok else "STALE", prefix, entry.number, entry.version, match.group(1),
                    prefix, target, match.group(3), want))

    invariants = (root / "foundations" / "invariants.md").read_text(encoding="utf-8")
    heading = None
    for line in invariants.split("\n"):
        if line.startswith("## "):
            heading = line[3:]
        found = re.match(r"^- \*\*Derives from:\*\* (.*)$", line)
        if found and found.group(1) != "none":
            for item in [i.strip() for i in found.group(1).split(" · ")]:
                match = re.fullmatch(r"%s-(\d{2,})@([0-9a-f]+)" % prefix, item)
                if not match:
                    continue
                checked += 1
                want = current.get(int(match.group(1)))
                if want != match.group(2):
                    stale += 1
                    print("STALE invariant %s derives from %s (current %s)" % (heading, item, want))
    print("relations and links checked: %d; stale or unread: %d" % (checked, stale))
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
