#!/bin/sh
# Runs the audit's counting command on crafted inputs; writes stdout, stderr and exit code per case into the directory given as $1.
OUT="$1"
cd "the worktree's root" || exit 1
I=".runs/executor-18/inputs"
run() {
  name="$1"; shift
  python -B process-audit/audit_count.py "$@" >"$OUT/$name.out" 2>"$OUT/$name.err"
  echo $? >"$OUT/$name.code"
}
run missing_locations --locations "$I/does_not_exist.json" --today 2026-11-19
run bad_json --locations "$I/bad.json" --today 2026-11-19
run empty_object --locations "$I/empty.json" --today 2026-11-19
run no_register --locations "$I/no_register.json" --today 2026-11-19
run bad_today --locations "$I/empty.json" --today 2026-13-45
run unknown_option --locations "$I/empty.json" --bogus
run missing_prices --locations "$I/no_register.json" --prices "$I/does_not_exist.md" --today 2026-11-19
run help --help
