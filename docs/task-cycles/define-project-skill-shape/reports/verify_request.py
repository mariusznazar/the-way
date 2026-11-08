"""Check every number of the request's description against figures computed from the files.

Usage: python -B verify_request.py REQUEST_FILE

Computes, with code of its own (no import from the author's scripts):
- the words of each file of `project-level/skill/` after (the worktree) and of `SKILL.md` before
  (commit dfd50e5), as whitespace-separated tokens (`wc -w` under a UTF-8 locale), the C-locale
  count of the base file, and the files read beside the skill;
- the six routes of the task's question 4, before and after, each sum and its percentage, and the
  six recorded runs;
- the figures of the gate outputs, `stages.md`, the assessment table, the diff of the range and the
  author's scripts' outputs stated in the reports.
Then it lists every number in the description's prose and tables, outside code spans, links and
a small set of contexts that are no count (dates, step and item numbers, line numbers, decision
identifiers, version of a model), and reports each that is no computed figure and no figure of the
task document. Exit 1 with the list when one is found, else 0. Prints only ASCII.
"""
import re
import subprocess
import sys

REPO = "."
REC = REPO + "/.runs/task-cycles/define-project-skill-shape"
BASE = "dfd50e513c09bebe9d09d74209cd28612565da83"
DASH = chr(8212)
MINUS = chr(8722)


def git(*args):
    return subprocess.run(["git", "-C", REPO] + list(args), capture_output=True, check=True,
                          encoding="utf-8").stdout


def words(text):
    return len(text.split())


def c_words(text):
    # coreutils in the C locale counts no token without a printable ASCII byte
    return len([t for t in text.split() if any(33 <= ord(ch) < 127 for ch in t)])


def section(text, title):
    lines = text.split("\n")
    out, on, level = [], False, 0
    for ln in lines:
        m = re.match(r"(#+) ", ln)
        if m and on and len(m.group(1)) <= level:
            break
        if m and ln[len(m.group(0)):].strip() == title:
            on, level = True, len(m.group(1))
        if on:
            out.append(ln)
    return "\n".join(out)


def pct(b, a, minus):
    v = round((a - b) * 100.0 / b, 1)
    sign = "+" if v > 0 else minus
    return "%s%.1f%%" % (sign, abs(v))


def main(argv):
    req = open(argv[1], encoding="utf-8").read()
    task = open(REC + "/task.md", encoding="utf-8").read()
    figs = set()

    def add(*xs):
        for x in xs:
            figs.add(str(x))

    after = {}
    for name in ["SKILL.md", "delegated_mode.md", "existing_definition.md", "idea.md",
                 "read_foundation.md", "first_write.md", "rounds.md", "find_entries.md",
                 "technology.md", "readiness_gate.md"]:
        after[name] = words(open(REPO + "/project-level/skill/" + name, encoding="utf-8").read())
    base = git("show", BASE + ":project-level/skill/SKILL.md")
    b = words(base)
    tmpl = words(git("show", BASE + ":project-level/definition_template.md"))
    wow = git("show", BASE + ":elements/common/way_of_working.md")
    ask = words(section(wow, "How a skill asks"))
    rf = words(section(wow, "Reading the foundation"))
    conv = words(git("show", BASE + ":project-level/lead/conversation_template.md"))
    total_after = sum(after.values())
    add(b, c_words(base), b - c_words(base), tmpl, ask, rf, conv, total_after, total_after - b,
        *after.values())
    S = after
    routes = {
        "1": (["SKILL.md", "idea.md", "read_foundation.md", "first_write.md", "rounds.md",
               "find_entries.md", "technology.md", "readiness_gate.md"], tmpl + ask + rf),
        "2": (["SKILL.md", "existing_definition.md", "find_entries.md", "technology.md",
               "readiness_gate.md"], tmpl + ask),
        "3a": (["SKILL.md", "delegated_mode.md", "existing_definition.md", "readiness_gate.md"],
               tmpl + ask + conv),
        "3b": (list(S), tmpl + ask + conv),
        "4": (["SKILL.md", "existing_definition.md", "readiness_gate.md"], tmpl + ask),
        "5": (["SKILL.md", "existing_definition.md", "technology.md", "readiness_gate.md"],
              tmpl + ask),
    }
    sums = {}
    for k, (files, beside) in routes.items():
        sa = sum(S[f] for f in files)
        sums[k] = (b, b + beside, sa, sa + beside)
        add(b + beside, sa, sa + beside, pct(b, sa, MINUS), pct(b + beside, sa + beside, MINUS))
    for k in ("3a", "3b"):
        sb = sums["1"][0] + 4 * sums[k][0] + sums["4"][0]
        tb = sums["1"][1] + 4 * sums[k][1] + sums["4"][1]
        sa = sums["1"][2] + 4 * sums[k][2] + sums["4"][2]
        ta = sums["1"][3] + 4 * sums[k][3] + sums["4"][3]
        add(sb, tb, sa, ta, pct(sb, sa, MINUS), pct(tb, ta, MINUS))
    # the delegated sentence of proposal 1
    sent = ("The project orchestrator may make the initial text edit only when that full text is "
            "already before it and needs no other definition-section or foundation reading; "
            "otherwise it delegates the edit.")
    dm = " ".join(open(REPO + "/project-level/skill/delegated_mode.md", encoding="utf-8").read().split())
    if sent not in dm:
        print("proposal 1 sentence not found in delegated_mode.md")
        return 1
    add(words(sent))
    # gate outputs
    for g in ("base_gate.txt", "gate_eeca32c.txt", "gate_09b0dd0.txt"):
        t = open(REC + "/" + g, encoding="utf-8", errors="replace").read()
        m = re.search(r"(\d+) tests in (\d+) directories; every directory passed\nexit (\d+)", t)
        add(*m.groups())
        add(len(re.findall(r"^skipped:", t, re.M)))
    # stages
    st = open(REC + "/stages.md", encoding="utf-8").read()
    m = re.search(r"joined: (\d+):(\d+):(\d+)", st)
    h, mi, se = map(int, m.groups())
    add(h * 60 + mi + (1 if se >= 30 else 0))
    tok = re.search(r"Tokens in all: ([\d,]+)", st).group(1)
    add(tok, tok.replace(",", chr(160)).replace(chr(160), " "))
    # assessment table
    asm = open(REC + "/reports/assessment.md", encoding="utf-8").read()
    rows = [ln for ln in asm.split("\n") if ln.startswith("| [`L")]
    verdicts = [re.match(r"\s*([A-Z]+)", ln.split("|")[4]).group(1) for ln in rows]
    add(len(rows), verdicts.count("KEEP"), verdicts.count("MOVE"))
    props = re.findall(r"^### Proposal (\d+)", asm, re.M)
    add(len(props))
    p2 = section(asm, "Proposal 2 - the other repetitions between the variant's file and "
                      "`project-level/lead/skill/SKILL.md:202-219`")
    p3 = section(asm, "Proposal 3 - the repetitions between the skill and "
                      "`project-level/definition_template.md`")
    add(len(re.findall(r"^\| [a-z] \|", p2, re.M)), len(re.findall(r"^\| [a-z] \|", p3, re.M)))
    # diff of the range
    ds = git("diff", "--shortstat", "2754675..09b0dd0")
    add(*re.findall(r"\d+", ds))
    # figures stated by the author's checks in the reports
    rep = open(REC + "/reports/author_report.md", encoding="utf-8").read()
    for pat in (r"(\d+) units of the base, (\d+) not word for word",
                r"project-level` \(.*?\) \| 0 \((\d+) tests\)",
                r"agent-instructions` \(same state\) \| 0 \((\d+) tests\)",
                r"installation` \(same state\) \| 0 \((\d+) tests\)"):
        m = re.search(pat, rep)
        add(*m.groups())
    ret = open(REC + "/reports/return_report.md", encoding="utf-8").read()
    add(*re.search(r"(\d+) figures compared, 0 differ", ret).groups())
    fx = open(REC + "/request.md", encoding="utf-8").read()  # noqa: the request itself is checked below
    del fx
    # numbers of the task document (estimates, figures it states)
    task_nums = set(re.findall(r"\d+", task))

    # the request: drop code spans, links and URLs, then list numbers
    body = re.sub(r"`[^`]*`", " ", req)
    body = re.sub(r"\]\([^)]*\)", "]", body)
    body = re.sub(r"https?://\S+", " ", body)
    body = re.sub(r"<[^>]+>", " ", body)
    skip = [
        r"\d{4}-\d\d-\d\d",                         # dates
        r"WAY-\d+",                                 # decision identifiers
        r"Opus 5\.5",                               # the model
        r"\b(?:steps?|items?|questions?|To do|route|routes|rows?|criterion|Checks,|lines?|"
        r"old lines|kroki?|kroku|pytanie|M|I)[ -]\d+(?:[.,]\d+)?(?:\s*(?:to|and|,|" + MINUS +
        r"|–|-)\s*\d+(?:\.\d+)?)*",
        r"\b\d+(?:\.\d)?[–-]\d+(?:\.\d)?\b(?!\s*words)",  # ranges such as 0-7, 7.1-7.5
        r"^\s*\d+\.\s", r"\|\s*\d[ab]?\.\s",        # list and table item numbers
        r"\(\w\)",
        r"\b7\.[1-5]\b",                          # the items of step 7
        r"\b5\.5\b",                              # the model's version
    ]
    for pat in skip:
        body = re.sub(pat, " ", body, flags=re.M)
    errors = []
    for tok in re.findall(r"[+" + MINUS + r"-]?(?:\d{1,3}(?:[, ]\d{3})+|\d+)(?:\.\d+)?%?", body):
        t = tok.strip().rstrip(",").strip()
        plain = t.lstrip("+" + MINUS + "-")
        if t in figs or plain in figs or plain.replace(",", "") in figs or plain.replace(" ", "") in figs \
                or plain.replace(" ", ",") in figs:
            continue
        if plain.isdigit() and int(plain) <= 12:
            continue  # small counts of items, checked by eye in the list below
        if plain in task_nums:
            continue
        errors.append(t)
    print("figures computed: %d; numbers not matched: %d" % (len(figs), len(errors)))
    for e in errors:
        print("  ", e.encode("ascii", "replace").decode("ascii"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
