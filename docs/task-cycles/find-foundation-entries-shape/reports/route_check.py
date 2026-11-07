#!/usr/bin/env python3
"""Route check of the rebuilt find-foundation-entries (own-work check of the author).

For each variant it lists the files an agent reaches from SKILL.md (the files SKILL.md names for
that variant, plus the common files), and checks, for a list of distinctive phrases of the base
text, that the phrase is on the route of every variant that needed it on the base and on no route
of a variant that did not. It also checks that the callers' own words stand in SKILL.md.
This is a presence check: it catches a lost or leaked fragment, not a changed meaning, which the
comparison in author.md covers. Run: python -I -B route_check.py
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SK = ROOT / "elements/common/skill"

COMMON_FILES = ["SKILL.md", "read.md", "build_table.md"]
ROUTES = {
    "definition": COMMON_FILES + ["definition_variant.md"],
    "task": COMMON_FILES + ["task_variant.md"],
}


def text(files):
    return "\n".join(" ".join((SK / f).read_text(encoding="utf8").split()) for f in files)


# phrase, variants that needed it on the base ("both", "definition", "task")
PHRASES = [
    ("Read `elements/common/way_of_working.md` in full", "both"),
    ("Read the source in full", "both"),
    ("Select and read the product's foundation by", "both"),
    ("the plan test in the decisions' template", "both"),
    ("Each candidate is a row", "both"),
    ("The last column names a concrete thing", "both"),
    ("A candidate from the material is a proposal", "both"),
    ("A settlement that an entry read in step 1 already states", "both"),
    ("The human accepts or rejects rows", "both"),
    ("resume from the first row whose state is neither", "both"),
    ("Write each state into the working table as soon as it is given", "both"),
    ("the section \"Projected foundation changes\" in full", "definition"),
    ("projected_mode.md", "definition"),
    ("Take each line of \"In scope\"", "definition"),
    ("as the template's working table", "definition"),
    ("Ask what the entry needs and the source does not give", "definition"),
    ("implication", "definition"),
    ("Hand the row to the skill of its element in projected mode", "definition"),
    ("reopen that entry with the human", "definition"),
    ("Tell the caller how many entries of each kind were written", "definition"),
    ("the breakdown of the project into tasks", "definition"),
    ("the section \"Settlements to record\" and its rule under", "task"),
    ("*Decisions in play*", "task"),
    ("Take each item of \"Need\"", "task"),
    ("never a change of the part map", "task"),
    ("column *State* after the template's columns", "task"),
    ("In place of step 4, a row that carries a choice", "task"),
    ("renumbering the rows that stay", "task"),
    ("Tell `refine-task` how many rows of each kind were kept", "task"),
    ("the task's cycle as the next reader", "task"),
]

# words the callers use for the variants (from the callers' files), which SKILL.md must hold
CALLER_WORDS = [
    ("project-level/task/skill/orchestrated_mode.md", "task mode"),
    ("product-guidelines/coding/hand_back.md", "task mode"),
    ("product-guidelines/styleguide/hand_back.md", "task mode"),
    ("product-guidelines/testing/hand_back.md", "task mode"),
    ("project-level/task/skill/find_settlements.md", "Settlements to record"),
    ("project-level/skill/SKILL.md", "Projected foundation changes"),
]


def main():
    bad = 0
    routes = {k: text(v) for k, v in ROUTES.items()}
    for phrase, who in PHRASES:
        for variant, body in routes.items():
            needs = who in ("both", variant)
            has = " ".join(phrase.split()) in body
            if needs and not has:
                bad += 1
                print("LOST  %-10s %s" % (variant, phrase))
            if not needs and has:
                bad += 1
                print("LEAK  %-10s %s" % (variant, phrase))
    skill = text(["SKILL.md"])
    for path, word in CALLER_WORDS:
        src = " ".join((ROOT / path).read_text(encoding="utf8").split())
        if word not in src:
            bad += 1
            print("CALLER %s does not hold %r" % (path, word))
        if word not in skill:
            bad += 1
            print("SKILL.md lacks the caller word %r (%s)" % (word, path))
    # every file SKILL.md names exists, and every file that exists is named
    named = [f for f in ["read.md", "build_table.md", "definition_variant.md", "task_variant.md"] if f in skill]
    if sorted(named) != sorted(["read.md", "build_table.md", "definition_variant.md", "task_variant.md"]):
        bad += 1
        print("SKILL.md names", named)
    present = sorted(p.name for p in SK.iterdir())
    if present != sorted(COMMON_FILES + ["definition_variant.md", "task_variant.md"]):
        bad += 1
        print("files in the directory:", present)
    # the variant file is named at steps 2, 4 and 5 as well as in the table and step 1 (WAY-265)
    for step in ("## 2. Build the table", "## 4. Row by row", "## 5. Close"):
        body = skill.split(step, 1)[1]
        nxt = body.find(" ## ")
        body = body if nxt < 0 else body[:nxt]
        for f in ("definition_variant.md", "task_variant.md"):
            if f not in body and not (step == "## 2. Build the table" and f not in body and False):
                bad += 1
                print("SKILL.md %s does not name %s" % (step, f))
    print("%d problem(s)" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
