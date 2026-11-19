#!/bin/bash
# usage: run_cases.sh <tag>; runs the crafted cases of the audit command and saves stdout, stderr and exit
tag=$1
cd the worktree's root
E=.runs/executor-16
out=$E/cases-$tag
mkdir -p $out $E/results-blocked-$tag/.count-2026-11-19.md.tmp
python - <<PY
import json, pathlib
base = pathlib.Path("$E").resolve()
loc = json.loads((base / "locations-crafted-$tag.json").read_text(encoding="utf-8"))
loc["the-way"]["audit_results"] = (base / "results-blocked-$tag").as_posix()
(base / "locations-blocked-$tag.json").write_text(json.dumps(loc), encoding="utf-8")
PY
python -B process-audit/audit_count.py --locations $E/locations-blocked-$tag.json --repository the-way --today 2026-11-19 > $out/blocked.out 2> $out/blocked.err; echo $? > $out/blocked.exit
python -B process-audit/audit_count.py --locations $E/locations-crafted-$tag.json --repository the-way --today 2026-11-19 > $out/crafted.out 2> $out/crafted.err; echo $? > $out/crafted.exit
python -B process-audit/audit_count.py --locations $E/locations-$tag.json --repository the-way --today 2026-11-19 > $out/template.out 2> $out/template.err; echo $? > $out/template.exit
python -B process-audit/audit_count.py --locations $E/locations-$tag.json --repository nosuch --today 2026-11-19 > $out/nokey.out 2> $out/nokey.err; echo $? > $out/nokey.exit
