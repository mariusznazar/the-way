"""Own-work check of correction 2.  Usage: python -B check.py FILE...
A sentence that names a row adopting an outside practice AND the state it is built in (accepted,
waiting, built, enters, waits) must carry the condition: the row repeats a choice the human made
between ways shown; or the sentence is about a row the agent derived."""
import re, sys
from pathlib import Path
row = re.compile(r"(row|candidate)[^.]{0,40}adopts? a practice from outside|adopts? a practice from outside[^.]{0,200}\b(row|candidate)", re.I)
state = re.compile(r"`accepted`|`waiting`|\bwaits?\b|\bbuilt\b|\benters\b", re.I)
cond = re.compile(r"repeats? a choice (the human made )?(among|between) ways shown|you derived|agent derived", re.I)
bad = 0
for f in sys.argv[1:]:
    t = re.sub(r"\s+", " ", Path(f).read_text(encoding="utf-8"))
    for sent in re.split(r"(?<=[.;]) (?=[A-Z-])", t):
        if row.search(sent) and state.search(sent) and not cond.search(sent):
            bad += 1; print("NO CONDITION:", f, "|", sent[:140])
print("sentences without the condition:", bad); sys.exit(1 if bad else 0)
