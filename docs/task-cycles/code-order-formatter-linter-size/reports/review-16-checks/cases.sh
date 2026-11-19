#!/bin/bash
cd .runs/review-16
run() { # tag script
  tag=$1; script=$2; o=cases-$tag; mkdir -p $o
  mkdir -p blocked-$tag/.count-2026-11-19.md.tmp
  python - <<PY
import json
loc=json.load(open("locations-crafted-$tag.json")); loc["the-way"]["audit_results"]=".runs/review-16/blocked-$tag"
json.dump(loc, open("locations-blocked-$tag.json","w"))
loc=json.load(open("locations-crafted-$tag.json")); del loc["the-way"]["problem_register"]
json.dump(loc, open("locations-noreg-$tag.json","w"))
PY
  python -B $script --locations locations-crafted-$tag.json --repository the-way --today 2026-11-19 > $o/crafted.out 2> $o/crafted.err; echo $? > $o/crafted.exit
  python -B $script --locations locations-blocked-$tag.json --repository the-way --today 2026-11-19 > $o/blocked.out 2> $o/blocked.err; echo $? > $o/blocked.exit
  python -B $script --locations locations-crafted-$tag.json --repository nosuch --today 2026-11-19 > $o/nokey.out 2> $o/nokey.err; echo $? > $o/nokey.exit
  python -B $script --locations locations-noreg-$tag.json --repository the-way --today 2026-11-19 > $o/noreg.out 2> $o/noreg.err; echo $? > $o/noreg.exit
  python -B $script --locations locations-crafted-$tag.json --repository the-way --today garbage > $o/baddate.out 2> $o/baddate.err; echo $? > $o/baddate.exit
  python -B $script --locations locations-crafted-$tag.json --repository the-way --today 2026-11-19 --prices nosuch.md > $o/noprices.out 2> $o/noprices.err; echo $? > $o/noprices.exit
  python -B $script --locations locations-crafted-$tag.json --repository the-way --today 2020-01-01 > $o/oldday.out 2> $o/oldday.err; echo $? > $o/oldday.exit
  cp results-crafted-$tag/count-latest.md $o/crafted-latest.md 2>/dev/null
}
run before base/process-audit/audit_count.py
run after ../../process-audit/audit_count.py
echo done > cases.done
