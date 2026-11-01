"""Write reports/word-counts.md: the words of the seven routes of task question 4, before and after.

Words as `wc -w` counts them (whitespace-separated), Markdown and frontmatter included; of a file
read by sections, the sections read (heading to the line before the next heading of the same or a
higher level). State "before" is commit 2f51e6c, state "after" the worktree.
"""
import subprocess
import sys

REPO = "C:/Storage/repos/the-way/.runs/worktrees/plan-project-skill-shape"
BASE = "2f51e6c31f5911ac8a0292a80a4f599bd4bd0092"
NL = chr(10)
P = "project-level/plan/skill/"
WOW = "elements/common/way_of_working.md"


def text_of(path, state):
    if state == "before":
        return subprocess.run(["git", "-C", REPO, "show", f"{BASE}:{path}"],
                              capture_output=True, check=True).stdout.decode("utf-8")
    with open(f"{REPO}/{path}", encoding="utf-8", newline="") as f:
        return f.read()


def section(text, heading):
    lines = text.split(NL)
    start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for j in range(start + 1, len(lines)):
        l = lines[j]
        if l.startswith("#") and len(l) - len(l.lstrip("#")) <= level:
            end = j
            break
    return NL.join(lines[start:end])


def count(entry, state):
    path = entry[0]
    text = text_of(path, state)
    if len(entry) == 2:
        text = section(text, entry[1])
        return f'{path} section "{entry[1].lstrip("# ")}"', len(text.split())
    return path, len(text.split())


def F(name):
    return (P + name,)


SKILL = F("SKILL.md")
TEMPLATE = ("project-level/plan/template.md",)
HAAS = (WOW, "## How a skill asks")
RTF = (WOW, "## Reading the foundation")
CONV = ("project-level/lead/conversation_template.md",)
READING = ("product-guidelines/reading.md",)
CRIT = [("elements/common/critique/SKILL.md",), ("elements/common/critique/prepare.md",),
        ("elements/common/critique/check.md",), ("elements/common/critique/settle.md",)]

# (title, reading note, skill files after, other files read in both states)
ROUTES = [
    ("1. New breakdown, the guidelines reading found nothing",
     "steps 0-7 run, a human-led session; the critique of step 6 runs (critique files read); no "
     "existing plan, no guidelines file",
     ["SKILL.md", "read.md", "reading_definition_and_plan.md", "cut_tasks.md", "assign_entries.md",
      "place_questions.md", "write_and_check.md", "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING] + CRIT),
    ("2. New breakdown with the guidelines file",
     "route 1 and the guidelines tasks of step 2 (guideline_tasks.md read)",
     ["SKILL.md", "read.md", "reading_definition_and_plan.md", "cut_tasks.md", "guideline_tasks.md",
      "assign_entries.md", "place_questions.md", "write_and_check.md", "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING] + CRIT),
    ("3. Resume of a draft from step 5",
     "steps 0, 5, 6, 7 run, a human-led session on an existing plan whose status reads draft; step 1 "
     "is carried out in the state after (existing_plan.md has the session go through read.md), so the "
     "foundation and the guidelines are read, and in the state before as well, by the rule below; "
     "the critique runs",
     ["SKILL.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md", "write_and_check.md",
      "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING] + CRIT),
    ("4. Human's correction to a handed-over plan, for example a split of a task",
     "steps 0, 1, 2, 3, 5, 6, 7 run, a human-led session on an existing plan; step 4 (no question "
     "moves) and the guidelines file are not read; the critique runs",
     ["SKILL.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md", "cut_tasks.md",
      "assign_entries.md", "write_and_check.md", "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING] + CRIT),
    ("5a. Narrow dispatched turn, one change, the agent reads its own steps",
     "a turn dispatched by lead-project that applies a requested change: steps 0, 1, 3, 5 run; the "
     "critique is requested through the conversation, so the critique files are not read; "
     "delegated_mode.md read",
     ["SKILL.md", "delegated_mode.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md",
      "assign_entries.md", "write_and_check.md"],
     [TEMPLATE, HAAS, RTF, READING, CONV]),
    ("5b. Narrow dispatched turn, one change, the agent reads everything",
     "the turn of 5a (steps 0, 1, 3, 5 run) reading every file of the skill, the guidelines file "
     "included",
     ["SKILL.md", "delegated_mode.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md",
      "cut_tasks.md", "guideline_tasks.md", "assign_entries.md", "place_questions.md",
      "write_and_check.md", "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING, CONV]),
    ("6. Dispatched turn of the hand over alone",
     "a turn dispatched by lead-project that only hands the plan over: steps 0 and 7 run (step 1 "
     "is carried out in both states by the rule below, as existing_plan.md has it); no critique run",
     ["SKILL.md", "delegated_mode.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md",
      "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING, CONV]),
    ("7. Dispatched recheck after the definition's gate",
     "a turn dispatched by lead-project that rechecks the plan from step 0: steps 0-7 run, no "
     "guidelines file; the critique is requested through the conversation, so the critique files are "
     "not read",
     ["SKILL.md", "delegated_mode.md", "existing_plan.md", "reading_definition_and_plan.md", "read.md",
      "cut_tasks.md", "assign_entries.md", "place_questions.md", "write_and_check.md",
      "critique_plan.md", "hand_over.md"],
     [TEMPLATE, HAAS, RTF, READING, CONV]),
]


def rows(entries, state):
    out, total = [], 0
    for e in entries:
        name, n = count(e, state)
        out.append((name, n))
        total += n
    return out, total


def fmt(rs):
    return NL.join(f"  - {name}: {n}" for name, n in rs)


def main(out):
    body, summary = [], []
    for title, note, skill_files, others in ROUTES:
        a_skill, a_s = rows([F(n) for n in skill_files], "after")
        a_oth, a_o = rows(others, "after")
        b_skill, b_s = rows([SKILL], "before")
        b_oth, b_o = rows(others, "before")
        body += [f"## {title}", "", f"Reading counted: {note}.", ""]
        for state, sk, s, oth, o in (("before", b_skill, b_s, b_oth, b_o), ("after", a_skill, a_s, a_oth, a_o)):
            body += [f"### {state.capitalize()}", "", f"Skill text, {s} words:", "", fmt(sk), "",
                     f"Read beside the skill, {o} words:", "", fmt(oth), "",
                     f"Total at the end of the run: {s + o} words.", ""]
        summary.append((title, b_s, b_s + b_o, a_s, a_s + a_o))
    head = ["# Word counts of the seven routes", "",
            "Words are counted as `wc -w` counts them (whitespace-separated), Markdown and frontmatter "
            "included; of a file read by sections, the sections read (the heading to the line before "
            "the next heading of the same or a higher level). The state \"before\" is commit 2f51e6c "
            "(`project-level/plan/skill/SKILL.md` is its only file of the skill); the state \"after\" "
            "is the worktree after the last change of a counted file. The definition, the plan and the "
            "product's files are outside the count.", "",
            "Rules of the count:", "",
            "- \"Skill text\" is `SKILL.md` and the files beside it that the route reads. \"Read beside "
            "the skill\" is what the route reads outside the skill: `project-level/plan/template.md` "
            "(step 0, every route), the section \"How a skill asks\" of `elements/common/way_of_working.md` "
            "(step 0), the section \"Reading the foundation\" of the same file and "
            "`product-guidelines/reading.md` (step 1, where step 1 runs), "
            "`project-level/lead/conversation_template.md` (a dispatched turn) and the four files of "
            "the critique (`elements/common/critique/SKILL.md`, `prepare.md`, `check.md`, `settle.md`), "
            "where the author runs the critique. The critic's own reading is another agent's context "
            "and is not counted.",
            "- Both states count the same files beside the skill; they differ only in the skill text. A "
            "route that skips a step in the state \"before\" skips it in the state \"after\" too, except "
            "that `existing_plan.md` has a session working on an existing plan go through `read.md` (step 1) "
            "before it goes on; step 1 is therefore carried out on every route that reads that file, in "
            "both states (see the next rule).",
            "- The rule for step 1 on a route that goes on from a later step (routes 3 and 6): the "
            "sentence of `existing_plan.md` has the session go through `read.md`, that is carry step 1 "
            "out, so the readings of step 1 count, the section \"Reading the foundation\" and "
            "`product-guidelines/reading.md` included. The recorded sessions ran the readiness check in "
            "14 of 14 and reached the foundation in 11, whatever the base's text said, so the state "
            "\"before\" counts step 1 as carried out too, on these two routes; the table above and the "
            "summary use that reading. The base's text read literally sent a resumed draft from the first "
            "unfinished step, past step 1; the figures of that literal reading are given beside, after the "
            "summary.",
            "- A file the skill reads for a condition that does not hold on the route is not counted: "
            "`guideline_tasks.md` only on routes 2 and 5b. Route 4 reads no `place_questions.md` (no "
            "question moves in a split of a task); where one moves, its words come on top.",
            "- Route 5 is counted in the two readings the task gives: 5a, the agent reads its own steps; "
            "5b, it reads everything.", "",
            "## Summary", "",
            "| Route | Skill text before | Total before | Skill text after | Total after | Change of the skill text | Change of the total |",
            "|---|---|---|---|---|---|---|"]
    for title, bs, bt, as_, at in summary:
        head.append(f"| {title} | {bs} | {bt} | {as_} | {at} | {100*(as_-bs)/bs:+.1f}% | {100*(at-bt)/bt:+.1f}% |")
    S = {s[0][:2]: (s[0], s[3]) for s in summary}
    lit = {}
    for title, note, skill_files, others in ROUTES:
        if title[:2] in ("3.", "6."):
            _, o = rows([e for e in others if e not in (RTF, READING)], "before")
            lit[title[:1]] = (summary[[s[0] for s in summary].index(title)], o)
    head += ["", "## The literal reading of the base on routes 3 and 6", "",
             "Read literally, the base sent a resumed draft from the first unfinished step, past step 1, so "
             "that a route which goes on from step 5 or hands over alone did not read the foundation or "
             "the guidelines. The figures of that reading, the state \"before\" without the section "
             "\"Reading the foundation\" and `product-guidelines/reading.md`, set beside the state \"after\" "
             "with step 1 carried out:", ""]
    for k in sorted(lit):
        (title, bs, bt, as_, at), o = lit[k]
        lt = bs + o
        head.append(f"- Route {k}: before, literal reading, {lt} words in total (skill text {bs}); after, step 1 carried out, "
                    f"{at} words in total (skill text {as_}); the change of the total is {100*(at-lt)/lt:+.1f}%. "
                    f"Before with step 1 carried out, as the table counts it: {bt} words, change {100*(at-bt)/bt:+.1f}%.")
    head += ["", "## Comparison with the estimates of the task (question 1 and its correction)", "",
             "The estimates are for the text of the skill alone, the first column of each state above.", "",
             f"- A fresh breakdown, estimated 2300-2900 words: route 1 reads {S['1.'][1]} and route 2 reads {S['2.'][1]}. Both inside.",
             f"- A narrow turn that reads its own steps, estimated 1650-1850 and corrected to 1800-2000 once the file of step 1 is counted: route 5a reads {S['5a'][1]}, inside the corrected range. Route 6 (the hand over alone, which reads the files of steps 0 and 1 and step 7) reads {S['6.'][1]}, below it: the estimate did not cover a turn of one step.",
             f"- A narrow turn that reads everything, estimated 2800-3250: route 5b reads {S['5b'][1]}, inside; route 7 (a recheck, no guidelines file) reads {S['7.'][1]}, inside.",
             f"- The cost of reading everything against today, estimated 450-900 words more than 2344: route 5b reads {S['5b'][1]-2344} more, inside.",
             f"- The not-chosen way of question 4 expected the realistic change of the skill text at -15% to +25%: the real range is {min(100*(s[3]-s[1])/s[1] for s in summary):+.1f}% to {max(100*(s[3]-s[1])/s[1] for s in summary):+.1f}% (routes 6 and 5b), so those two fall outside it; the totals with the files read beside the skill change by {min(100*(s[4]-s[2])/s[2] for s in summary):+.1f}% to {max(100*(s[4]-s[2])/s[2] for s in summary):+.1f}%, step 1 counted in both states on routes 3 and 6; counted in the state after alone the totals of routes 3 and 6 would rise (see the literal reading above).",
             "- The task's 'about 170 words on every route with an existing plan' is the file `read.md` alone (141 words); what the sentence of `existing_plan.md` sets off on routes 3 and 6 is that file plus the section 'Reading the foundation' (492 words) and `product-guidelines/reading.md` (1141 words), 1774 words together with the file.",
             "- Figures that the task states and that the files confirm: `SKILL.md` 2344 words at 2f51e6c, `project-level/plan/template.md` 1881 words, the section 'How a skill asks' 208 words. The file of step 1 (`read.md`) is 141 words against the estimate of about 170 for the reading of step 1.",
             ""]
    with open(out, "w", encoding="utf-8", newline=NL) as f:
        f.write(NL.join(head + body) + NL)
    for title, bs, bt, as_, at in summary:
        print(title[:3], bs, bt, as_, at)


if __name__ == "__main__":
    main(sys.argv[1])
