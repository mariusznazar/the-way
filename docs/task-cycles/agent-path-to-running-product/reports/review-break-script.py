"""Apply one deliberate break to readiness_check.py in the given worktree (reviewer's scratch)."""
import sys
path, which = sys.argv[1] + "/project-level/readiness_check.py", sys.argv[2]
text = open(path, encoding="utf-8", newline="").read()
if which == "B1":
    old = "    findings += check_technology(by_name[TECHNOLOGY], by_name[PROJECTED])\n"
    new = ("    technology = check_technology(by_name[TECHNOLOGY], by_name[PROJECTED])\n"
           "    if not before_approval:  # BREAK: an approved definition keeps its older list\n"
           "        technology = [f for f in technology\n"
           "                      if not f.message.startswith(\"no choice item begins with\")]\n"
           "    findings += technology\n")
elif which == "B2":
    old = "        if not any(text.startswith(mark) for text in texts):\n"
    new = ("        if not any(mark in line for _, line in content(section)):  # BREAK: any line\n")
elif which == "B3":
    old = "    for mark in AGENT_PATH_MARKS:\n        if not any(text.startswith(mark) for text in texts):\n"
    new = ("    for mark in AGENT_PATH_MARKS[:1]:  # BREAK: one of the three only\n"
           "        if not any(text.startswith(m) for text in texts for m in AGENT_PATH_MARKS):\n")
assert text.count(old) == 1, which
open(path, "w", encoding="utf-8", newline="").write(text.replace(old, new))
print("applied", which)
