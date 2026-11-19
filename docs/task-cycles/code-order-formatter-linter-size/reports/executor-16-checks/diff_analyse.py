"""Run analyse of the audit_count in the directory given on seeded random input and dump the result."""
import json, random, sys
from datetime import date
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
import audit_count as ac
import problem_register

LEVELS = ["no problem", "Minor", "Important", "Critical"]
COSTS = ["nothing", "steps", "stage", "round", "human"]

class Stub:
    def commit(self, text):
        if text.startswith("x"):
            return None, "no such commit " + text
        return text.upper(), None
    def holds(self, pin, fix):
        n = sum(map(ord, pin + fix)) % 3
        return [(True, None), (False, None), (None, "cannot compare " + pin)][n]

def hexs(rng):
    return "".join(rng.choice("0123456789abcdef") for _ in range(40))

def build(seed):
    rng = random.Random(seed)
    repos = ["the-way", "prod"]
    cycles, records = [], []
    for i in range(rng.randint(0, 8)):
        repo = rng.choice(repos)
        rec = hexs(rng)
        later = [hexs(rng) for _ in range(rng.randint(0, 2))]
        if records and rng.random() < 0.2:
            later.append(rng.choice(records)[1])  # a commit shared with another cycle
        copies = {c: rng.choice(["unknown", "2026-0%d-1%d" % (rng.randint(1, 9), rng.randint(0, 9))]) for c in [rec, *later]}
        cy = ac.Cycle(repo, f"f{i}", rec, copies[rec], later, copies)
        cy.pin = rng.choice([None, "x" + hexs(rng)[:7], hexs(rng)[:7], "abc1234"])
        cycles.append(cy)
        records.append((repo, rec))
        records.extend((repo, l) for l in later)
    issues = []
    for j in range(rng.randint(0, 6)):
        issues.append((f"issue-{j}", rng.choice(["open", "fixed", "dropped"]), rng.choice(["none", "x" + hexs(rng)[:7], hexs(rng)[:7], "abc1234"])))
    classes = ["c-a", "c-b", "c-c"]
    problems, refused_problems, refused = [], [], []
    for k in range(rng.randint(0, 14)):
        if records and rng.random() < 0.75:
            repo, rec = rng.choice(records)
        else:
            repo, rec = rng.choice(repos + ["gone"]), hexs(rng)
        issue = rng.choice([i[0] for i in issues] + ["no-issue"]) if issues else "no-issue"
        problems.append(problem_register.Problem(k + 1, repo, rec, rng.choice(classes), rng.choice(LEVELS), rng.choice(COSTS), issue))
    for k in range(rng.randint(0, 5)):
        if records and rng.random() < 0.7:
            repo, rec = rng.choice(records)
            rec = rec.upper() if rng.random() < 0.3 else rec
        else:
            repo, rec = "the-way", rng.choice(["short", hexs(rng)])
        issue = rng.choice([i[0] for i in issues] + ["", "no-issue"]) if issues else ""
        refused_problems.append((repo, rec, issue))
        refused.append((repo, rec, f"row {k + 50} of `Problems`", "refused"))
    register = ac.Register(classes=classes, issues=issues, problems=problems, refused_problems=refused_problems, refused=refused)
    reads = [ac.Read("the-way", [c for c in cycles if c.repository == "the-way"]), ac.Read("prod", [c for c in cycles if c.repository == "prod"])]
    return reads, register

out = []
for seed in range(3000):
    reads, register = build(seed)
    today = date(2026, 3, 5)
    a = ac.analyse(reads, register, Stub(), today)
    out.append([a.cycle_rows, a.fixed_rows, a.open_rows, a.dropped_rows, a.cost_rows, a.unknown, a.held])
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"))
print("seeds", len(out), "nonempty open rows", sum(1 for o in out if o[2]), "fixed", sum(1 for o in out if o[1]), "unknown", sum(1 for o in out if o[5]))
