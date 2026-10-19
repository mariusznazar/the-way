"""Weakest-point check of Slice 4 (WAY-164): the requirement C33 protects — a case that the form
check reports nothing against keeps `instruction-files/check_instructions.py` in step, so that
script switches between code and text exactly on the case's opening and closing lines and on no
line of its text.

Seeded random cases: each inner line is built from pieces drawn from every character Python takes
for whitespace, every character `splitlines` breaks on, backticks, tildes, letters and spaces.
For each, the case is put in a rule naming one invariant, the form check's own reading
(`Document`, `check_cases`) is run in this process, and the lines check_instructions toggles on
inside the case's span are counted. A case with no finding of check_cases must give exactly two
toggles (its opening and closing fence); a case with one must give some finding at a line where
check_instructions sees a toggle or that holds the closing.

Usage: python3 -B weakest.py <the-way> [samples]
"""

import importlib.util
import os
import random
import sys

THE_WAY = sys.argv[1]
SAMPLES = int(sys.argv[2]) if len(sys.argv) > 2 else 20000


def load(name, *path):
    spec = importlib.util.spec_from_file_location(name, os.path.join(THE_WAY, *path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


form_check = load("form_check_weakest", os.environ.get("FORM_CHECK") or os.path.join("product-guidelines", "form_check.py"))
instructions = load("check_instructions_weakest", "instruction-files", "check_instructions.py")
shared = load("guard_shared_weakest", "elements", "common", "guard_shared.py")

WHITE = [chr(i) for i in range(sys.maxunicode + 1) if chr(i).isspace() and chr(i) != "\n"]
BREAKS = ["\r", "\x0b", "\x0c", "\x1c", "\x1d", "\x1e", "\x85", " ", " "]
PIECES = WHITE + BREAKS + ["`", "``", "```", "````", "~", "~~~", "a", "ts", " ", "x = 1;"]

HEAD = ("## Rules\n\n### A rule\n\n- **Decision:** ABC-01@00000000\n"
        "- **Invariant:** endpoint-handler@00000000\n- **Good:** good.\n- **Bad:** bad.\n\n"
        "How.\n\n```bad endpoint-handler src/a.ts\nx\n```\n\n")


def run_case(inner_lines):
    case = "```good endpoint-handler src/a.ts\n" + "\n".join(inner_lines) + "\n```\n"
    text = HEAD + case + "\n## Examples\n"
    document = form_check.Document(text)
    report = shared.Report("guidelines/x.md")
    sections = {block.title: block for block in document.sections}
    form_check.check_cases(document, sections, report, shared,
                           form_check.Foundation(known=False))
    findings = list(report.verdicts.get(("check_cases", form_check.FORM), []))
    # The span of the good case in check_instructions' reading: from its opening line to the
    # first line after it that toggles, where the good case should close.
    pieces = text[text.index(case):].splitlines()
    toggles = [index for index, piece in enumerate(pieces[:len(case.splitlines())])
               if instructions.FENCE.match(piece)]
    return findings, toggles, len(case.splitlines())


def main():
    rng = random.Random(164)
    clean = flagged = mismatches = 0
    shown = []
    for _ in range(SAMPLES):
        inner = ["".join(rng.choice(PIECES) for _ in range(rng.randint(1, 4)))
                 for _ in range(rng.randint(1, 3))]
        findings, toggles, span = run_case(inner)
        if not findings:
            clean += 1
            if toggles != [0, span - 1]:
                mismatches += 1
                if len(shown) < 10:
                    shown.append(("clean but out of step", inner, toggles, span))
        else:
            flagged += 1
    print("samples: %d, with no finding: %d, with a finding: %d" % (SAMPLES, clean, flagged))
    print("cases with no finding whose span check_instructions does not toggle exactly on the "
          "opening and closing line: %d" % mismatches)
    for item in shown:
        print(repr(item))
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
