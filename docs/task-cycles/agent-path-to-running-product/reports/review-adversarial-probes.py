"""Adversarial probes of the mark rule of readiness_check (reviewer's scratch)."""
import sys, os
sys.dont_write_bytecode = True
root = sys.argv[1]
sys.path.insert(0, os.path.join(root, "project-level"))
import test_readiness_check as t
import readiness_check as rc

L = "- logs: Logi — held by: ARC-03/1"
I = "- interface: Przegladarka — held by: ARC-04/1"
D = "- development data: Dane — held by: ARC-05/1"
B = "- Jezyk — held by: ARC-01/1"
cases = {
    "baseline: all three": "\n".join([B, L, I, D]),
    "fence at column 0 holding logs": "\n".join([B, "```", L, "```", I, D]),
    "fence indented after a nested item, holding logs": "\n".join([B, "  - note", "  ```", L, "  - x", "  ```", I, D]),
    "mark with no name": "\n".join([B, "- logs: — held by: ARC-03/1", I, D]),
    "mark with no space after colon": "\n".join([B, "- logs:Logi — held by: ARC-03/1", I, D]),
    "two spaces after the list dash": "\n".join([B, "-  logs: Logi — held by: ARC-03/1", I, D]),
    "asterisk list marker": "\n".join([B, "* logs: Logi — held by: ARC-03/1", I, D]),
    "mark in backticks": "\n".join([B, "- `logs:` Logi — held by: ARC-03/1", I, D]),
    "fullwidth colon": "\n".join([B, "- logs\uff1a Logi — held by: ARC-03/1", I, D]),
    "nbsp inside development data": "\n".join([B, L, I, "- development\u00a0data: Dane — held by: ARC-05/1"]),
    "two logs items": "\n".join([B, L, L.replace("ARC-03", "ARC-06"), I, D]),
    "html comment holding logs": "\n".join([B, "<!--", L, "-->", I, D]),
}
for name, body in cases.items():
    for mode in ("before approval", "approved"):
        if mode == "before approval":
            text = t.definition(status="Status: ready for gate", gate="", bodies={"Technology": body})
            f = rc.check(text, before_approval=True)
        else:
            text = t.definition(bodies={"Technology": body})
            f = rc.check(text)
        print("%-50s %-16s %s" % (name, mode, [(x.condition, x.message[:60]) for x in f] or "PASS"))
