"""Invariant tests of the form check of guidelines, `product-guidelines/form_check.py`.

Each test builds a product in a temporary git repository — a decision log, an invariants file, a
part map, the files `## Where in code` points to and one or more files `guidelines/<name>.md` —
runs the command as a subprocess on it and asserts its exit code, its report lines
`guidelines/<name>.md:<line>: error: …` and the lines of its record.

Inputs, expected fingerprints and expected fragments of the report are written out below, never
computed by the code under test (WAY-69): each fingerprint was computed once, by hand, with
`relation-model/fingerprint.py` from the binding sentence it stands beside. A valid styleguide and
a valid file of a discipline the-way has no template of pass first; every other test breaks one
thing in them, so a test that sees an error sees the one its break caused. The tests that replace
a line name the line they expect there, so a fixture whose lines move fails loudly instead of
making a check pass for the wrong reason.

The coding guidelines — a general file `guidelines/coding.md` and the file of the kind `endpoint`,
`guidelines/coding-endpoint.md` — follow the two required forms of the coding template, with its
headings, header lines, table columns and values of *Status* written out as that template gives
them. A coding test counts only an error the valid coding files do not give themselves, so that an
error a form check without the coding template reports for them — the name of a file of a kind,
first of all — never stands in for the error a test asks for.

Run from the root of the-way:
    python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
THE_WAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(THE_WAY, "product-guidelines", "form_check.py")

# Stands, in the text of guidelines a test writes, for the product's root as an absolute path.
PRODUCT_ROOT = "{product-root}"

FORM = "guidelines-form/1"
REFERENCES = "guidelines-reference-current/1"

# Binding sentences of the fixture's foundation, each with its fingerprint written out.
ROLES_DECISION = ("The background role primary marks the main action of a screen, and the text "
                  "role primary-text stands on it.")
ROLES_FP = "daa9cf8d"
ROLES_REWORDED = ("The background role primary marks the one main action of a screen, and the "
                  "text role primary-text stands on it.")
ROLES_REWORDED_FP = "cca35182"
MUTED_DECISION = "The role muted marks what matters less than what is around it."
MUTED_FP = "9bb0959d"
DEPARTURE_DECISION = ("The product's styleguide drops the rules on design tokens, focus, contrast, "
                      "shared controls, global values, sources of values and the kitchen-sink "
                      "page until the product draws screens of its own.")
DEPARTURE_FP = "8503cafa"
FONT_DECISION = "The product draws its text in one font of its own."
FONT_FP = "7ba1b4bb"
FIXTURES_DECISION = "Each test of the product sets up its data through the product's fixtures."
FIXTURES_FP = "016b5b2a"
ROLE_MEANING = ("No screen of the web interface uses a colour role in a meaning other than the "
                "one its decision gives.")
ROLE_MEANING_FP = "a2557545"
ROLE_MEANING_REWORDED = ("No screen of the web interface uses a colour role in any meaning other "
                         "than the one its decision gives.")
ROLE_MEANING_REWORDED_FP = "cbbaa72e"
PAIR = "Every background role of the styleguide's table names the text role that stands on it."
PAIR_FP = "169d4c67"

# The binding sentences of the coding guidelines' foundation. ABC-09 stays out of the log: the
# tests of references name it as a decision the log does not hold.
LINT_DECISION = ("Every file of the product's code passes the linter ESLint with the product's "
                 "configuration.")
LINT_DECISION_FP = "646b8156"
FORMAT_DECISION = "Every file of the product's code stands as the formatter Prettier writes it."
FORMAT_DECISION_FP = "c17d8fa7"
AUDIT_DECISION = ("No dependency of the product carries a known vulnerability that npm audit "
                  "reports.")
AUDIT_DECISION_FP = "5300274d"
# Designates the exemplar of the kind `endpoint`, its path and its kind in backticks, wrapped over
# lines as a log wraps its sentences: their whitespace collapsed, the sentence holds both.
EXEMPLAR_DECISION = ("The file\n`src/api/orders/route.ts` is the exemplar of the kind\n`endpoint`, "
                     "and every endpoint validates its input with the shared schema and answers "
                     "through the shared handler.")
EXEMPLAR_DECISION_FP = "9a9314b5"
KIND_ONLY_DECISION = "The kind `endpoint` takes the file that answers orders as its exemplar."
KIND_ONLY_DECISION_FP = "89fdd602"
PATH_ONLY_DECISION = "The file `src/api/orders/route.ts` is the exemplar of the kind endpoint."
PATH_ONLY_DECISION_FP = "3e313c51"
TWO_EXEMPLARS_DECISION = ("The files `src/api/orders/route.ts` and `src/api/users/route.ts` are "
                          "both exemplars of the kind `endpoint`.")
TWO_EXEMPLARS_DECISION_FP = "d478f129"
BARE_PATH_DECISION = "The file src/api/orders/route.ts is the exemplar of the kind `endpoint`."
BARE_PATH_DECISION_FP = "cdcdd48d"
NO_AUDIT_DECISION = ("The product runs no audit of its dependencies until it takes in its first "
                     "dependency.")
NO_AUDIT_DECISION_FP = "1fff448b"
LINT = "Every file of the product's code passes ESLint with no error."
LINT_FP = "2838ab3c"
FORMAT = "Every file of the product's code stands as Prettier writes it."
FORMAT_FP = "d03c47d0"
AUDIT = "npm audit reports no known vulnerability in a dependency of the product."
AUDIT_FP = "04c6cde8"
VALIDATES = "Every file of the kind endpoint validates its input with the shared schema."
VALIDATES_FP = "9666b706"
HANDLER = "Every file of the kind endpoint answers through the shared handler."
HANDLER_FP = "8c2ca199"
LOCATION = "Every file of the kind endpoint lies under the directory src/api."
LOCATION_FP = "f58796ac"
# The product's copy of the invariant of guidelines that checks their form, as the template of
# guidelines gives its sentence.
GUIDELINES_FORM = (
    "Every file `guidelines/<name>.md` holds, in their order, the header lines, sections, rules, "
    "rule fields and tables that the template of guidelines and the template of its discipline "
    "require at the commit of the-way the repository uses — the commit checked, in the-way itself, "
    "and the pinned commit, in a product — each with the values and the links those templates give "
    "it, with a name that agrees with its *Discipline*, each section or rule it drops reading "
    "`none —` with a decision of the log and that decision's fingerprint, each part it names being "
    "a part of the map, and each path under `## Where in code` naming something git tracks.")
GUIDELINES_FORM_FP = "7196030f"

# Fingerprints that differ from the current one only in their last character.
ROLES_STALE = "daa9cf80"
ROLE_MEANING_STALE = "a2557540"
DEPARTURE_STALE = "8503cafb"


def decision(number, ver, question, binding, change):
    """A decision version in the form of the decisions template."""
    lines = ["### ABC-%02d/%d — %s" % (number, ver, question), ""]
    if binding is not None:
        lines += [binding, ""]
    lines += ["- **Change:** " + change, "- **Scope:** web", "- **Based on:** none",
              "- **Relations:** none",
              "- **Verification:** level 2 — an agent compares the change with the decision:",
              "  - complies: a screen follows the decision;",
              "  - violates: a screen goes against it.",
              "- **Review when:** none", "- **Origin:** none",
              "- **Approved by:** Anna, 2026-09-01", "",
              "*%s:* one role carries one meaning." % ("Rationale" if ver == 1
                                                      else "Rationale for change"),
              "*Rejected:* none considered"]
    return "\n".join(lines)


def log(*versions):
    return "# Decision log\n\nIntro.\n\n" + "\n\n".join(versions) + "\n"


ABC_01 = decision(1, 1, "Which roles mark the main action?", ROLES_DECISION, "new decision")
ABC_01_REWORDED = decision(1, 2, "Which roles mark the main action?", ROLES_REWORDED,
                           "new wording")
ABC_02 = decision(2, 1, "Which role marks what matters less?", MUTED_DECISION, "new decision")
ABC_03 = decision(3, 1, "Which rules of the styleguide does the product drop?",
                  DEPARTURE_DECISION, "new decision")
ABC_04 = decision(4, 1, "Which font does the product draw its text in?", FONT_DECISION,
                  "new decision")
ABC_04_REPEALED = decision(4, 2, "Which font does the product draw its text in?", None, "repeal")
ABC_05 = decision(5, 1, "How does a test set up its data?", FIXTURES_DECISION, "new decision")
CODING_DECISIONS = (
    decision(10, 1, "Which linter reads the product's code?", LINT_DECISION, "new decision"),
    decision(11, 1, "Which formatter writes the product's code?", FORMAT_DECISION, "new decision"),
    decision(12, 1, "How are the product's dependencies audited?", AUDIT_DECISION, "new decision"),
    decision(13, 1, "Which file is the exemplar of an endpoint?", EXEMPLAR_DECISION,
             "new decision"),
    decision(14, 1, "Which file answering orders is an exemplar?", KIND_ONLY_DECISION,
             "new decision"),
    decision(15, 1, "Which file is an exemplar, by its path?", PATH_ONLY_DECISION, "new decision"),
    decision(16, 1, "Which files are exemplars together?", TWO_EXEMPLARS_DECISION, "new decision"),
    decision(17, 1, "Which file is an exemplar, named bare?", BARE_PATH_DECISION, "new decision"),
    decision(18, 1, "Does the product audit its dependencies yet?", NO_AUDIT_DECISION,
             "new decision"),
)

LOG = log(ABC_01, ABC_02, ABC_03, ABC_04, ABC_04_REPEALED, ABC_05, *CODING_DECISIONS)
# The log the commit merged onto holds: ABC-01 reworded there, and only there.
LOG_ONTO = log(ABC_01, ABC_02, ABC_03, ABC_04, ABC_04_REPEALED, ABC_05, *CODING_DECISIONS,
               ABC_01_REWORDED)


def invariant(identifier, ver, sentence):
    return "\n".join(["## %s/%d" % (identifier, ver), "", sentence, "",
                      "- **Method:** `python -B tests/check_roles.py`", "- **Rests on:** none",
                      "- **Derives from:** ABC-01@" + ROLES_FP, "- **Part:** web",
                      "- **Correction:** none"])


def invariants(*entries):
    return "# Invariants\n\n" + "\n\n".join(entries + (
        "## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n|---|---|---|\n"
        "| old-pair | merged with another entry | background-pair |",
        "## Quarantined invariants\n\n| Identifier | Version | Until |\n|---|---|---|")) + "\n"


CODING_INVARIANTS = (invariant("lint-clean", 1, LINT), invariant("format-clean", 1, FORMAT),
                     invariant("audit-clean", 1, AUDIT),
                     invariant("endpoint-validates", 1, VALIDATES),
                     invariant("endpoint-handler", 1, HANDLER),
                     invariant("endpoint-location", 1, LOCATION),
                     invariant("guidelines-form", 1, GUIDELINES_FORM))
INVARIANTS = invariants(invariant("role-meaning", 1, ROLE_MEANING),
                        invariant("background-pair", 1, PAIR), *CODING_INVARIANTS)
# The invariants file the commit merged onto holds: role-meaning reworded there, and only there.
INVARIANTS_ONTO = invariants(invariant("role-meaning", 2, ROLE_MEANING_REWORDED),
                             invariant("background-pair", 1, PAIR), *CODING_INVARIANTS)

PART_MAP = """# Part map

## web — The web interface

The part answers for the screens of the product.

- **Files:** src/
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none
"""

FOUNDATION = {
    "foundations/decisions.md": LOG,
    "foundations/invariants.md": INVARIANTS,
    "foundations/part_map.md": PART_MAP,
    "src/tokens.css": ":root { --primary: #1d4ed8; }\n",
    "src/components/button.tsx": "export const Button = () => null;\n",
    "tests/fixtures.py": "PLAYER = {}\n",
    "src/api/schema.ts": "export const schema = { parse: (input: unknown) => input };\n",
    "src/api/handler.ts": "export const handle = (answer: Function) => answer;\n",
    "src/api/orders/route.ts": ('import { handle } from "../handler";\n'
                                'import { schema } from "../schema";\n'
                                "export const POST = handle((input: unknown) => "
                                "schema.parse(input));\n"),
    "src/api/users/route.ts": ('import { handle } from "../handler";\n'
                               'import { schema } from "../schema";\n'
                               "export const POST = handle((input: unknown) => "
                               "schema.parse(input));\n"),
    "src/api/legacy/route.ts": "export const POST = (input: unknown) => input;\n",
}

def case(which, identifier, path, *lines):
    """A test case of a rule: a fenced block whose info string reads `<which> <identifier>
    <path>`, holding `lines` as the whole text of the file at that path, and a blank line."""
    return "```%s %s %s\n%s\n```\n\n" % (which, identifier, path, "\n".join(lines))


# A styleguide holding every part its template requires; seven required rules are dropped by
# ABC-03. Each rule naming an invariant other than `guidelines-form` gives a good and a bad case
# for it. The comments give the line each piece starts on.
TITLE = "# Styleguide guidelines — the web interface\n\n"                          # 1
HEADER = "- **Discipline:** styleguide\n- **Applies to:** web\n\n"                  # 3
WHEN = "## When to read\n\nBefore changing a screen of the web interface.\n\n"      # 6
ROLES = ("## Roles\n\n"                                                             # 10
         "| Role | Kind | Meaning for the user | Text on it | Decision |\n"
         "|---|---|---|---|---|\n"
         "| primary | background | this is the main action of the screen | primary-text | "
         "ABC-01@" + ROLES_FP + " |\n"                                              # 14
         "| primary-text | text | this text stands on the main action | — | "
         "ABC-01@" + ROLES_FP + " |\n"
         "| muted | other | this matters less than what is around it | — | "
         "ABC-02@" + MUTED_FP + " |\n\n")                                           # 16
EACH_ROLE = ("### Each role in its meaning\n\n"                                     # 20
             "- **Decision:** ABC-01@" + ROLES_FP + " · ABC-02@" + MUTED_FP + "\n"  # 22
             "- **Invariant:** role-meaning@" + ROLE_MEANING_FP + "\n"              # 23
             "- **Good:** the main action of a form uses `primary`.\n"
             "- **Bad:** a warning uses `primary`.\n\n"
             "Use each role only in the meaning its decision gives.\n\n")           # 27
EACH_ROLE_CASES = (case("good", "role-meaning", "src/components/save.tsx",          # 29
                        'export const Save = () => <button className="bg-primary '
                        'text-primary-text">Save</button>;')
                   + case("bad", "role-meaning", "src/components/warning.tsx",      # 33
                          'export const Warning = () => <p className="bg-primary '
                          'text-primary-text">Careful</p>;'))
EACH_ROLE += EACH_ROLE_CASES
BACKGROUND_CASES = (case("good", "background-pair", "src/tokens.css",               # 46
                         ":root { --primary: #1d4ed8; --primary-text: #ffffff; }")
                    + case("bad", "background-pair", "src/tokens.css",              # 50
                           ":root { --primary: #1d4ed8; }"))
BACKGROUND = ("### Every background with its text\n\n"                              # 37
              "- **Decision:** ABC-01@" + ROLES_FP + "\n"                           # 39
              "- **Invariant:** background-pair@" + PAIR_FP + "\n"                  # 40
              "- **Good:** `primary` stands in the table with `primary-text`.\n"
              "- **Bad:** `primary` stands in the table with no text role.\n\n"
              "Write every background role with the text role that stands on it.\n\n"  # 44
              + BACKGROUND_CASES)
DROPPED = ("No value in place of a design token", "Visible focus", "Contrast of every pair",
           "States of shared controls", "A fault of one screen is fixed in its component",
           "Every value with its source", "The kitchen-sink page")


def dropped(name):
    return "### %s\n\nnone — ABC-03@%s\n\n" % (name, DEPARTURE_FP)


RULES = ("## Rules\n\n" + EACH_ROLE + BACKGROUND                                    # 18
         + "".join(dropped(name) for name in DROPPED))                              # 54 … 80
EXAMPLES = ("## Examples\n\n"                                                       # 82
            "### Mockups\n\n"
            "A mockup is a pattern to compare against; meanings come from this file.\n\n"  # 86
            "### Plan of a user-interface change\n\n"
            "Settle the library, then the values, then one screen, then its states.\n\n")
WHERE = "## Where in code\n\n- `src/tokens.css`\n- `src/components`\n"              # 92, 94
STYLEGUIDE = TITLE + HEADER + WHEN + ROLES + RULES + EXAMPLES + WHERE
STYLEGUIDE_FILE = "guidelines/styleguide-web.md"

# Guidelines of a discipline the-way gives no template of: the common form alone.
TESTING = """# Testing guidelines — the tests of the web interface

- **Discipline:** testing
- **Applies to:** web

## When to read

Before writing a test of the web interface.

## Rules

### Test data through fixtures

- **Decision:** ABC-05@016b5b2a
- **Invariant:** none
- **Good:** a test sets up its player through the fixtures.
- **Bad:** a test writes rows straight into the store of data.

Set up each test's data through the product's fixtures.

## Examples

### Branch names

The team names its branches after their tasks.

## Where in code

- `tests/fixtures.py`
"""
TESTING_FILE = "guidelines/testing.md"


def rule(name, decisions, invariants_named, good, bad, how):
    """A rule under `## Rules`, its four fields and how to apply it, with no case after it."""
    return ("### %s\n\n- **Decision:** %s\n- **Invariant:** %s\n- **Good:** %s\n- **Bad:** %s\n\n"
            "%s\n\n" % (name, decisions, invariants_named, good, bad, how))


# The coding guidelines: the general file and the file of the kind `endpoint`, in the two required
# forms of the coding template with their headings, header lines, table columns and the values of
# *Status* as they stand there. Every rule names an invariant, and gives a good and a bad case for
# each invariant it names.
LINTER_HEAD = rule("Linter", "ABC-10@" + LINT_DECISION_FP, "lint-clean@" + LINT_FP,
                   "a function declares no variable it does not read.",
                   "a function declares a variable it never reads.",
                   "Run ESLint with the product's configuration on every file of the code.")
LINTER_CASES = (case("good", "lint-clean", "src/api/sum.ts",
                     "export const sum = (a: number, b: number) => a + b;")
                + case("bad", "lint-clean", "src/api/sum.ts",
                       "export const sum = (a: number, b: number) => {",
                       "  const unused = 1;",
                       "  return a + b;",
                       "};"))
FORMATTER = (rule("Formatter", "ABC-11@" + FORMAT_DECISION_FP, "format-clean@" + FORMAT_FP,
                  "a file stands as Prettier writes it.",
                  "a file keeps spacing Prettier would change.",
                  "Let Prettier write every file of the code.")
             + case("good", "format-clean", "src/api/sum.ts",
                    "export const sum = (a: number, b: number) => a + b;")
             + case("bad", "format-clean", "src/api/sum.ts",
                    "export const sum=(a:number,b:number)=>a+b"))
AUDIT_HEAD = rule("Dependency audit", "ABC-12@" + AUDIT_DECISION_FP, "audit-clean@" + AUDIT_FP,
                  "the product depends on a version npm audit flags nothing in.",
                  "the product depends on a version npm audit flags.",
                  "Run npm audit before taking in a dependency.")
AUDIT_CASES = (case("good", "audit-clean", "package.json",
                    '{"dependencies": {"left-pad": "1.3.0"}}')
               + case("bad", "audit-clean", "package.json",
                      '{"dependencies": {"event-stream": "3.3.6"}}'))
KINDS_ROW = ("| endpoint | `guidelines/coding-endpoint.md` | before adding or changing an "
             "endpoint |")
CODING = ("# Coding guidelines — the product\n\n"
          "- **Discipline:** coding\n- **Applies to:** web\n\n"
          "## When to read\n\nBefore changing the product's code.\n\n"
          "## Kinds of code\n\n"
          "| Kind | File | When to read |\n|---|---|---|\n" + KINDS_ROW + "\n\n"
          "## Rules\n\n" + LINTER_HEAD + LINTER_CASES + FORMATTER + AUDIT_HEAD + AUDIT_CASES
          + "## Examples\n\n### Short functions\n\nThe team keeps a function short enough to read "
            "at a glance.\n\n"
          "## Where in code\n\n- `src/api`\n")
CODING_FILE = "guidelines/coding.md"

EXEMPLAR_ROW = "| `src/api/orders/route.ts` | exemplar | ABC-13@" + EXEMPLAR_DECISION_FP + " |"
COPY_ROW = "| `src/api/users/route.ts` | copy | — |"
DO_NOT_COPY_ROW = "| `src/api/legacy/route.ts` | do not copy | — |"
VALIDATES_HEAD = rule("Input validated with the shared schema",
                      "ABC-13@" + EXEMPLAR_DECISION_FP, "endpoint-validates@" + VALIDATES_FP,
                      "an endpoint parses its input with the shared schema.",
                      "an endpoint reads its input unchecked.",
                      "Parse the input with the shared schema before reading it.")
VALIDATES_GOOD = case("good", "endpoint-validates", "src/api/carts/route.ts",
                      'import { handle } from "../handler";',
                      'import { schema } from "../schema";',
                      "export const POST = handle((input: unknown) => schema.parse(input));")
VALIDATES_BAD = case("bad", "endpoint-validates", "src/api/carts/route.ts",
                     'import { handle } from "../handler";',
                     "export const POST = handle((input: unknown) => input);")
HANDLER_HEAD = rule("Under the API, through the shared handler",
                    "ABC-13@" + EXEMPLAR_DECISION_FP,
                    "endpoint-handler@%s · endpoint-location@%s" % (HANDLER_FP, LOCATION_FP),
                    "an endpoint under `src/api` answers through the shared handler.",
                    "an endpoint elsewhere answers on its own.",
                    "Put each endpoint under `src/api` and answer through the shared handler.")
HANDLER_CASES = (case("good", "endpoint-handler", "src/api/carts/route.ts",
                      'import { handle } from "../handler";',
                      "export const POST = handle((input: unknown) => input);")
                 + case("bad", "endpoint-handler", "src/api/carts/route.ts",
                        "export const POST = (input: unknown) => new Response(String(input));"))
LOCATION_CASES = (case("good", "endpoint-location", "src/api/carts/route.ts",
                       'import { handle } from "../handler";',
                       "export const POST = handle((input: unknown) => input);")
                  + case("bad", "endpoint-location", "src/carts/route.ts",
                         'import { handle } from "../api/handler";',
                         "export const POST = handle((input: unknown) => input);"))
CODING_ENDPOINT = ("# Coding guidelines — endpoint\n\n"
                   "- **Discipline:** coding\n- **Applies to:** web\n\n"
                   "## When to read\n\nBefore adding or changing an endpoint.\n\n"
                   "## Files of this kind\n\n"
                   "| File | Status | Decision |\n|---|---|---|\n"
                   + EXEMPLAR_ROW + "\n" + COPY_ROW + "\n" + DO_NOT_COPY_ROW + "\n\n"
                   "## Rules\n\n" + VALIDATES_HEAD + VALIDATES_GOOD + VALIDATES_BAD
                   + HANDLER_HEAD + HANDLER_CASES + LOCATION_CASES
                   + "## Examples\n\n### Names of inputs\n\nThe exemplar names each input after "
                     "what it holds.\n\n"
                   "## Where in code\n\n- `src/api/orders/route.ts`\n")
CODING_ENDPOINT_FILE = "guidelines/coding-endpoint.md"
CODING_FILES = {CODING_FILE: CODING, CODING_ENDPOINT_FILE: CODING_ENDPOINT}


def line_of(text, line):
    """The number (from 1) of the one line of `text` reading `line`."""
    lines = text.split("\n")
    if lines.count(line) != 1:
        raise AssertionError("the fixture holds the line %r %d times, not once"
                             % (line, lines.count(line)))
    return lines.index(line) + 1


def with_line(text, number, expected, new):
    """`text` with its line `number` (from 1) replaced by `new`; the line must read `expected`."""
    lines = text.split("\n")
    if lines[number - 1] != expected:
        raise AssertionError("line %d of the fixture reads %r, not %r"
                             % (number, lines[number - 1], expected))
    lines[number - 1] = new
    return "\n".join(lines)


def replaced(text, old, new):
    """`text` with the one occurrence of `old` replaced by `new`."""
    if text.count(old) != 1:
        raise AssertionError("the fixture holds %r %d times, not once" % (old, text.count(old)))
    return text.replace(old, new)


# The errors each set of valid files gives, by (files, options), filled as the tests run.
BASELINES = {}


class FormCheckTestCase(unittest.TestCase):
    def check(self, guidelines, options=("--merge-onto", "none"), onto=None, untracked=None):
        """Runs the form check on a product whose base commit holds FOUNDATION, and whose main
        branch then gains a commit holding `guidelines` ({path: text}). Given `onto` ({path:
        text}), a branch `onto` leaves the base commit with those files changed, so that a merge
        onto it takes them. `untracked` files are written into the working tree and never added.
        PRODUCT_ROOT in the text of guidelines stands for the product's root, an absolute path
        with forward slashes, the repository standing in a folder named `product`.
        Returns the exit code, the output, the record's lines and the options given."""
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory, \
                tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as outside:
            root = os.path.join(os.path.realpath(directory), "product")
            os.makedirs(root)

            def write(files):
                for path, text in files.items():
                    full = os.path.join(root, *path.split("/"))
                    os.makedirs(os.path.dirname(full), exist_ok=True)
                    with open(full, "w", encoding="utf-8", newline="\n") as handle:
                        handle.write(text)

            def git(*arguments):
                subprocess.run(["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com",
                                "-c", "core.autocrlf=false"] + list(arguments),
                               cwd=root, check=True, capture_output=True)

            git("init", "-q", "-b", "main")
            write(FOUNDATION)
            git("add", "-A")
            git("commit", "-q", "-m", "foundation")
            if onto is not None:
                git("checkout", "-q", "-b", "onto")
                write(onto)
                git("add", "-A")
                git("commit", "-q", "-m", "onto")
                git("checkout", "-q", "main")
            write({path: text.replace(PRODUCT_ROOT, root.replace(os.sep, "/"))
                   for path, text in guidelines.items()})
            git("add", "-A")
            git("commit", "-q", "-m", "guidelines")
            if untracked:
                write(untracked)
            record = os.path.join(os.path.realpath(outside), "guidelines.jsonl")
            environment = dict(os.environ, PYTHONIOENCODING="utf-8")
            run = subprocess.run([sys.executable, "-B", SCRIPT] + list(options)
                                 + ["--record", record], cwd=root, capture_output=True,
                                 text=True, encoding="utf-8", errors="replace", env=environment)
            lines = []
            if os.path.isfile(record):
                with open(record, encoding="utf-8") as handle:
                    lines = [json.loads(line) for line in handle if line.strip()]
            return run.returncode, run.stdout + run.stderr, lines, tuple(options)

    def errors(self, output, path):
        """(line, message) of every error the output reports in the file `path`, or in any of
        the paths of a tuple `path`; an error reported under a path with no line has line None."""
        paths = path if isinstance(path, tuple) else (path,)
        pattern = re.compile(r"^(?:%s)(?::(\d+))?: error: (.*)$"
                             % "|".join(re.escape(each) for each in paths), re.MULTILINE)
        return [(int(line) if line else None, message)
                for line, message in pattern.findall(output)]

    def assert_reported(self, result, path, line=None, fragments=(), record=FORM):
        """The run exits 1, reports an error in `path` (or in one of the paths of a tuple) — at
        `line` where given — whose message holds each fragment of `fragments` (a tuple standing
        for any of its members), and its record gives `record` a `fail`."""
        code, output, lines, _ = result
        self.assertEqual(code, 1, output)
        found = [message for at, message in self.errors(output, path)
                 if line is None or at == line]
        for fragment in fragments:
            alternatives = fragment if isinstance(fragment, tuple) else (fragment,)
            found = [message for message in found
                     if any(alternative in message for alternative in alternatives)]
        self.assertTrue(found, "no error in %s%s naming %r:\n%s"
                        % (path, "" if line is None else ":%d" % line, fragments, output))
        self.assertIn("fail", [entry.get("verdict") for entry in lines
                               if entry.get("invariant") == record], lines)

    def assert_reported_anew(self, result, path, baseline=None, line=None, fragments=(),
                             record=FORM):
        """As assert_reported, counting only an error that the run on the valid files
        `baseline` ({path: text}, by default CODING_FILES), with the same options, does not
        report in the same file with the same message. A broken fixture is thus never taken as
        reported for an error its valid form carries too — one the form check gives it before
        the check under test exists, such as a name it does not yet know."""
        code, output, lines, options = result
        self.assertEqual(code, 1, output)
        valid = self.baseline_errors(CODING_FILES if baseline is None else baseline, options)
        paths = path if isinstance(path, tuple) else (path,)
        found = [message for each in paths for at, message in self.errors(output, each)
                 if (line is None or at == line) and (each, message) not in valid]
        for fragment in fragments:
            alternatives = fragment if isinstance(fragment, tuple) else (fragment,)
            found = [message for message in found
                     if any(alternative in message for alternative in alternatives)]
        self.assertTrue(found, "no error in %s%s naming %r that the valid files lack:\n%s"
                        % (path, "" if line is None else ":%d" % line, fragments, output))
        self.assertIn("fail", [entry.get("verdict") for entry in lines
                               if entry.get("invariant") == record], lines)

    def baseline_errors(self, files, options):
        """{(path, message)} of every error the run on `files` with `options` reports in a file
        of `files`, run once per set and kept for the rest of the run."""
        key = (tuple(sorted(files.items())), tuple(options))
        if key not in BASELINES:
            _, output, _, _ = self.check(files, options)
            BASELINES[key] = {(path, message) for path in list(files) + ["guidelines"]
                              for _, message in self.errors(output, path)}
        return BASELINES[key]

    def assert_clean(self, result):
        """The run exits 0, reports no error, and its record gives `pass` to what it records:
        the checks of form with no option, the checks of references with `--merge-onto`."""
        code, output, lines, options = result
        self.assertEqual(code, 0, output)
        self.assertNotIn(": error:", output)
        self.assertNotIn("fail", [entry.get("verdict") for entry in lines
                                  if entry.get("invariant") in (FORM, REFERENCES)], lines)
        recorded = REFERENCES if "--merge-onto" in options else FORM
        self.assertIn("pass", [entry.get("verdict") for entry in lines
                               if entry.get("invariant") == recorded], lines)


class Fixtures(FormCheckTestCase):
    def test_the_valid_fixtures_pass(self):
        """The styleguide and the guidelines of a discipline with no template, as written above,
        hold no error: every other test breaks one thing in them. Were they to fail, no error
        another test sees could be told from one the fixture itself carries."""
        # invariant: guidelines-check-form/1
        # invariant: guidelines-check-carrier/1
        # invariant: guidelines-check-colour-pair/1
        # invariant: guidelines-check-reference-target/1
        # invariant: guidelines-check-stale-reference/1
        # invariant: guidelines-check-code-path/1
        # invariant: guidelines-check-example-files/1
        self.assertEqual(STYLEGUIDE.count("```good "), 2)
        self.assertEqual(STYLEGUIDE.count("```bad "), 2)
        files = {STYLEGUIDE_FILE: STYLEGUIDE, TESTING_FILE: TESTING}
        for options in ((), ("--merge-onto", "none")):
            with self.subTest(options=options):
                self.assert_clean(self.check(files, options))
        self.assert_clean(self.check(files, ("--merge-onto", "onto"),
                                     onto={"src/other.css": "a {}\n"}))


class Form(FormCheckTestCase):
    def test_a_missing_or_misplaced_header_line_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Applies to", replaced(STYLEGUIDE, "- **Applies to:** web\n", ""), ("Applies to",)),
            ("no Discipline", replaced(TESTING, "- **Discipline:** testing\n", ""), ("Discipline",)),
            ("header lines swapped",
             replaced(STYLEGUIDE, "- **Discipline:** styleguide\n- **Applies to:** web\n",
                      "- **Applies to:** web\n- **Discipline:** styleguide\n"),
             (("Discipline", "Applies to"),)),
        )
        for name, text, fragments in cases:
            path = TESTING_FILE if text.startswith("# Testing") else STYLEGUIDE_FILE
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_missing_or_misplaced_section_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no When to read", STYLEGUIDE_FILE,
             TITLE + HEADER + ROLES + RULES + EXAMPLES + WHERE, ("When to read",)),
            ("no Roles in a styleguide", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + RULES + EXAMPLES + WHERE, ("Roles",)),
            ("no Examples", TESTING_FILE,
             replaced(TESTING, "## Examples\n\n### Branch names\n\nThe team names its branches "
                               "after their tasks.\n\n", ""), ("Examples",)),
            ("no Where in code", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + ROLES + RULES + EXAMPLES.rstrip("\n") + "\n",
             ("Where in code",)),
            ("Roles before When to read", STYLEGUIDE_FILE,
             TITLE + HEADER + ROLES + WHEN + RULES + EXAMPLES + WHERE,
             (("Roles", "When to read"),)),
            ("Where in code before Examples", STYLEGUIDE_FILE,
             TITLE + HEADER + WHEN + ROLES + RULES + WHERE + "\n" + EXAMPLES.rstrip("\n") + "\n",
             (("Where in code", "Examples"),)),
        )
        for name, path, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_missing_or_misplaced_required_rule_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Visible focus", replaced(STYLEGUIDE, dropped("Visible focus"), ""),
             ("Visible focus",)),
            ("no Every background with its text", replaced(STYLEGUIDE, BACKGROUND, ""),
             ("Every background with its text",)),
            ("Contrast of every pair before Visible focus",
             with_line(with_line(STYLEGUIDE, 58, "### Visible focus", "### Contrast of every pair"),
                       62, "### Contrast of every pair", "### Visible focus"),
             (("Visible focus", "Contrast of every pair"),)),
        )
        for name, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                                     fragments=fragments)

    def test_a_missing_or_misplaced_rule_field_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Good in a styleguide", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 24, "- **Good:** the main action of a form uses `primary`.",
                       ""), ("Good",)),
            ("no Bad in guidelines with no template", TESTING_FILE,
             with_line(TESTING, 17, "- **Bad:** a test writes rows straight into the store of "
                                    "data.", ""), ("Bad",)),
            ("no Invariant field", TESTING_FILE,
             with_line(TESTING, 15, "- **Invariant:** none", ""), ("Invariant",)),
            ("Bad before Good", STYLEGUIDE_FILE,
             with_line(with_line(STYLEGUIDE, 24,
                                 "- **Good:** the main action of a form uses `primary`.",
                                 "- **Bad:** a warning uses `primary`."),
                       25, "- **Bad:** a warning uses `primary`.",
                       "- **Good:** the main action of a form uses `primary`."),
             (("Good", "Bad"),)),
        )
        for name, path, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path, fragments=fragments)

    def test_a_drop_with_any_text_but_a_departing_decision_is_reported(self):
        # invariant: guidelines-check-form/1
        line = "none — ABC-03@" + DEPARTURE_FP
        cases = (
            ("a reason in place of a decision", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 60, line, "none — the browser draws focus")),
            ("none alone", STYLEGUIDE_FILE, with_line(STYLEGUIDE, 60, line, "none")),
            ("a decision with no fingerprint", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 60, line, "none — ABC-03")),
            ("another marker", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 60, line, "n/a — ABC-03@" + DEPARTURE_FP)),
            ("text beside the departure", STYLEGUIDE_FILE,
             with_line(STYLEGUIDE, 60, line, line + "\n\nThe browser draws focus.")),
            ("a dropped section with a reason", TESTING_FILE,
             replaced(TESTING, "Before writing a test of the web interface.",
                      "none — no one reads it first")),
        )
        for name, path, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_drop_naming_its_departing_decision_passes(self):
        """The control of the test above: a section and a rule dropped as the template has it."""
        # invariant: guidelines-check-form/1
        text = replaced(TESTING, "Before writing a test of the web interface.",
                        "none — ABC-03@" + DEPARTURE_FP)
        self.assert_clean(self.check({TESTING_FILE: text}, ()))

    def test_a_part_the_map_does_not_hold_is_reported(self):
        # invariant: guidelines-check-form/1
        self.assert_reported(
            self.check({STYLEGUIDE_FILE: with_line(STYLEGUIDE, 4, "- **Applies to:** web",
                                                   "- **Applies to:** web · mobile")}, ()),
            STYLEGUIDE_FILE, line=4, fragments=("mobile",))
        self.assert_reported(
            self.check({TESTING_FILE: replaced(TESTING, "- **Applies to:** web",
                                               "- **Applies to:** mobile")}, ()),
            TESTING_FILE, line=4, fragments=("mobile",))
        # Only a styleguide names a part in its file's name (WAY-167); a file of another
        # discipline named after a part is a name that disagrees with its Discipline, below.
        path = "guidelines/styleguide-mobile.md"
        with self.subTest(path):
            self.assert_reported(self.check({path: STYLEGUIDE}, ()), path, fragments=("mobile",))

    def test_a_file_whose_name_and_discipline_disagree_is_reported(self):
        """A styleguide stands in `guidelines/styleguide-<part>.md`, and guidelines of any other
        discipline in `guidelines/<discipline>.md` alone, never under a part's name (WAY-167)."""
        # invariant: guidelines-check-form/1
        cases = (
            ("guidelines/styleguide-web.md", TESTING),
            ("guidelines/web.md", TESTING),
            ("guidelines/testing-web.md", TESTING),
            ("guidelines/testing-mobile.md", TESTING),
            ("guidelines/look-web.md", STYLEGUIDE),
            ("guidelines/styleguide.md", STYLEGUIDE),
            ("guidelines/testing-web.md", STYLEGUIDE),
            ("guidelines/testing.md", STYLEGUIDE),
        )
        for path, text in cases:
            with self.subTest(path=path, discipline="testing" if text is TESTING
                              else "styleguide"):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_file_whose_name_follows_its_discipline_passes(self):
        """The control of the test above: the same texts under names that agree with them."""
        # invariant: guidelines-check-form/1
        for path, text in (("guidelines/testing.md", TESTING),
                           ("guidelines/styleguide-web.md", STYLEGUIDE)):
            with self.subTest(path):
                self.assert_clean(self.check({path: text}, ()))


class Carrier(FormCheckTestCase):
    def test_a_rule_naming_no_decision_is_reported(self):
        # invariant: guidelines-check-carrier/1
        cases = (
            ("a styleguide's rule", STYLEGUIDE_FILE, with_line(
                STYLEGUIDE, 39, "- **Decision:** ABC-01@" + ROLES_FP, "- **Decision:** none")),
            ("a styleguide's rule naming an invariant only", STYLEGUIDE_FILE, with_line(
                STYLEGUIDE, 39, "- **Decision:** ABC-01@" + ROLES_FP,
                "- **Decision:** background-pair@" + PAIR_FP)),
            ("a rule of guidelines with no template", TESTING_FILE, replaced(
                TESTING, "- **Decision:** ABC-05@" + FIXTURES_FP, "- **Decision:** none")),
        )
        for name, path, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({path: text}, ()), path)

    def test_a_styleguide_rule_naming_no_invariant_is_reported(self):
        # invariant: guidelines-check-carrier/1
        further = ("### Spacing on a grid\n\n- **Decision:** ABC-02@" + MUTED_FP + "\n"
                   "- **Invariant:** none\n- **Good:** a card keeps the grid's gap.\n"
                   "- **Bad:** a card sets a gap of its own.\n\nKeep every gap on the grid.\n\n")
        # The rule's cases go with the invariant they are cases of, so that no case names an
        # invariant the rule no longer names.
        cases = (
            ("a required rule", replaced(with_line(STYLEGUIDE, 40,
                                                   "- **Invariant:** background-pair@" + PAIR_FP,
                                                   "- **Invariant:** none"),
                                         BACKGROUND_CASES, "")),
            ("a required rule naming a decision only", replaced(with_line(
                STYLEGUIDE, 40, "- **Invariant:** background-pair@" + PAIR_FP,
                "- **Invariant:** ABC-01@" + ROLES_FP), BACKGROUND_CASES, "")),
            ("a further rule of the product", replaced(STYLEGUIDE, "## Examples\n",
                                                       further + "## Examples\n")),
        )
        for name, text in cases:
            with self.subTest(name):
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE)

    def test_a_rule_naming_no_invariant_outside_a_styleguide_passes(self):
        """The control of the test above: TESTING's rule names `none` in *Invariant*."""
        # invariant: guidelines-check-carrier/1
        self.assertIn("- **Invariant:** none\n", TESTING)
        self.assert_clean(self.check({TESTING_FILE: TESTING}, ()))

    def test_a_decision_of_the_roles_the_meaning_rule_does_not_name_is_reported(self):
        # invariant: guidelines-check-carrier/1
        text = with_line(STYLEGUIDE, 22, "- **Decision:** ABC-01@%s · ABC-02@%s"
                         % (ROLES_FP, MUTED_FP), "- **Decision:** ABC-01@" + ROLES_FP)
        self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                             fragments=("ABC-02",))

    def test_a_decision_of_the_roles_passes_where_the_meaning_rule_is_dropped(self):
        """The control of the test above: the rule "Each role in its meaning" dropped by a
        decision leaves the table's decisions unnamed by it, and that is no error."""
        # invariant: guidelines-check-carrier/1
        text = replaced(STYLEGUIDE, EACH_ROLE, dropped("Each role in its meaning"))
        self.assert_clean(self.check({STYLEGUIDE_FILE: text}, ()))


class ColourPair(FormCheckTestCase):
    def test_a_background_without_a_text_role_is_reported(self):
        # invariant: guidelines-check-colour-pair/1
        row = ("| primary | background | this is the main action of the screen | primary-text | "
               "ABC-01@" + ROLES_FP + " |")
        for text_on_it in ("", "—", "muted", "primary", "ink"):
            with self.subTest(text_on_it=text_on_it):
                text = with_line(STYLEGUIDE, 14, row, row.replace(
                    "| primary-text |", "| %s |" % text_on_it if text_on_it else "|  |"))
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                                     line=14)


# Where a reference can stand: (where, line, the line as STYLEGUIDE holds it, the line with the
# reference `%s` in it).
PLACES = (
    ("a Decision field", 39, "- **Decision:** ABC-01@" + ROLES_FP,
     "- **Decision:** ABC-01@" + ROLES_FP + " · %s"),
    ("an Invariant field", 40, "- **Invariant:** background-pair@" + PAIR_FP,
     "- **Invariant:** background-pair@" + PAIR_FP + " · %s"),
    ("a row of Roles", 16, "| muted | other | this matters less than what is around it | — | "
     "ABC-02@" + MUTED_FP + " |",
     "| muted | other | this matters less than what is around it, as %s has it | — | "
     "ABC-02@" + MUTED_FP + " |"),
    ("a rule's prose", 44, "Write every background role with the text role that stands on it.",
     "Write every background role with the text role that stands on it, as %s has it."),
    ("inline code in a rule's prose", 44,
     "Write every background role with the text role that stands on it.",
     "Write every background role with the text role that stands on it, as `%s` has it."),
    ("an example", 86, "A mockup is a pattern to compare against; meanings come from this file.",
     "A mockup is a pattern to compare against; meanings come from %s."),
    ("a departure", 60, "none — ABC-03@" + DEPARTURE_FP, "none — %s"),
)


class ReferenceTarget(FormCheckTestCase):
    def test_a_reference_to_an_entry_not_in_force_is_reported_wherever_it_stands(self):
        # invariant: guidelines-check-reference-target/1
        targets = (
            ("a decision the log does not hold", "ABC-09@0123abcd"),
            ("a repealed decision", "ABC-04@" + FONT_FP),
            ("an invariant the file does not hold", "missing-pair@0123abcd"),
            ("a withdrawn invariant", "old-pair@0123abcd"),
        )
        for where, line, old, new in PLACES:
            for target, reference in targets:
                with self.subTest(where=where, target=target):
                    text = with_line(STYLEGUIDE, line, old, new % reference)
                    self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                         line=line, fragments=(reference,), record=REFERENCES)

    def test_a_reference_whose_fingerprint_is_not_eight_hexadecimal_characters_is_reported(self):
        # invariant: guidelines-check-reference-target/1
        references = ("ABC-01@daa9", "ABC-01@DAA9CF8D", "ABC-01@daa9cf8d0", "ABC-01@zz",
                      "role-meaning@v2", "old-pair@x")
        for where, line, old, new in PLACES:
            for reference in references:
                with self.subTest(where=where, reference=reference):
                    text = with_line(STYLEGUIDE, line, old, new % reference)
                    self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                         line=line, fragments=(reference,), record=REFERENCES)

    def test_a_versioned_package_name_or_a_bare_identifier_is_no_reference(self):
        """`react@18`, `tailwindcss@4` and `lucide-react@0` fit neither form of a reference, and
        an identifier with no `@` is a bare mention; none is reported."""
        # invariant: guidelines-check-reference-target/1
        line = "Write every background role with the text role that stands on it."
        for mention in ("`react@18`", "react@18", "`tailwindcss@4`", "lucide-react@0",
                        "ABC-01", "ABC-01/1", "role-meaning", "old-pair", "ABC-09"):
            with self.subTest(mention=mention):
                text = with_line(STYLEGUIDE, 44, line, line[:-1] + ", as %s has it." % mention)
                self.assert_clean(self.check({STYLEGUIDE_FILE: text}))

    def test_a_reference_in_fenced_code_is_ignored(self):
        # invariant: guidelines-check-reference-target/1
        # invariant: guidelines-check-stale-reference/1
        example = "A mockup is a pattern to compare against; meanings come from this file."
        for fence in ("```", "~~~"):
            with self.subTest(fence=fence):
                block = "\n".join([
                    example, "", fence + "text",
                    "ABC-09@0123abcd · ABC-04@%s · missing-pair@0123abcd · old-pair@x" % FONT_FP,
                    "ABC-01@%s · role-meaning@%s · left-pad@0123abcd" % (ROLES_STALE,
                                                                         ROLE_MEANING_STALE),
                    fence])
                text = with_line(STYLEGUIDE, 86, example, block)
                self.assert_clean(self.check({STYLEGUIDE_FILE: text}))


class StaleReference(FormCheckTestCase):
    def test_a_stale_reference_on_the_commit_checked_is_reported_wherever_it_stands(self):
        # invariant: guidelines-check-stale-reference/1
        cases = (
            ("a Decision field", 22, "- **Decision:** ABC-01@%s · ABC-02@%s" % (ROLES_FP, MUTED_FP),
             "- **Decision:** ABC-01@%s · ABC-02@%s" % (ROLES_STALE, MUTED_FP), "ABC-01",
             ROLES_FP),
            ("an Invariant field", 23, "- **Invariant:** role-meaning@" + ROLE_MEANING_FP,
             "- **Invariant:** role-meaning@" + ROLE_MEANING_STALE, "role-meaning",
             ROLE_MEANING_FP),
            ("a row of Roles", 14, "| primary | background | this is the main action of the "
             "screen | primary-text | ABC-01@" + ROLES_FP + " |",
             "| primary | background | this is the main action of the screen | primary-text | "
             "ABC-01@" + ROLES_STALE + " |", "ABC-01", ROLES_FP),
            ("a rule's prose", 27, "Use each role only in the meaning its decision gives.",
             "Use each role only in the meaning role-meaning@%s guards." % ROLE_MEANING_STALE,
             "role-meaning", ROLE_MEANING_FP),
            ("an example", 86,
             "A mockup is a pattern to compare against; meanings come from this file.",
             "A mockup is a pattern to compare against; meanings come from ABC-01@%s."
             % ROLES_STALE, "ABC-01", ROLES_FP),
            ("a departure", 60, "none — ABC-03@" + DEPARTURE_FP,
             "none — ABC-03@" + DEPARTURE_STALE, "ABC-03", DEPARTURE_FP),
        )
        for where, line, old, new, entry, current in cases:
            with self.subTest(where):
                text = with_line(STYLEGUIDE, line, old, new)
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}), STYLEGUIDE_FILE,
                                     line=line, fragments=(entry, current), record=REFERENCES)

    def test_a_reference_a_merge_leaves_stale_is_reported(self):
        """The commit merged onto rewords a decision, or an invariant, that the branch never
        touched: the references the branch carries are current on its own commit and stale in
        the foundation the merge leaves."""
        # invariant: guidelines-check-stale-reference/1
        cases = (
            ("a decision reworded on the commit merged onto",
             {"foundations/decisions.md": LOG_ONTO}, 22, "ABC-01", ROLES_REWORDED_FP),
            ("an invariant reworded on the commit merged onto",
             {"foundations/invariants.md": INVARIANTS_ONTO}, 23, "role-meaning",
             ROLE_MEANING_REWORDED_FP),
        )
        for name, onto, line, entry, current in cases:
            with self.subTest(name):
                self.assert_reported(
                    self.check({STYLEGUIDE_FILE: STYLEGUIDE}, ("--merge-onto", "onto"), onto=onto),
                    STYLEGUIDE_FILE, line=line, fragments=(entry, current), record=REFERENCES)

    def test_a_reference_a_merge_leaves_stale_is_current_on_the_commit_checked(self):
        """The control of the test above: the same branch, checked with no commit to merge onto,
        holds no error, so what the test above sees comes from the merge."""
        # invariant: guidelines-check-stale-reference/1
        for onto in ({"foundations/decisions.md": LOG_ONTO},
                     {"foundations/invariants.md": INVARIANTS_ONTO}):
            with self.subTest(onto=sorted(onto)):
                self.assert_clean(self.check({STYLEGUIDE_FILE: STYLEGUIDE}, onto=onto))


class CodePath(FormCheckTestCase):
    def test_a_path_outside_what_git_tracks_is_reported(self):
        # invariant: guidelines-check-code-path/1
        line = "- `src/tokens.css`"
        paths = ("../outside.md", "src/../src/tokens.css", "/etc/passwd", r"C:\x", "C:/x",
                 r"\\host\share\x", "//host/share/x", ":(glob)**", "http://host/x",
                 "src/missing.css", "src/draft.css")
        for path in paths:
            with self.subTest(path=path):
                text = with_line(STYLEGUIDE, 94, line, "- `%s`" % path)
                fragments = () if "\\" in path else (path,)
                self.assert_reported(
                    self.check({STYLEGUIDE_FILE: text}, (),
                               untracked={"src/draft.css": ":root {}\n"}),
                    STYLEGUIDE_FILE, line=94, fragments=fragments)

    def test_a_path_out_of_the_repository_is_reported_though_its_remainder_is_tracked(self):
        """An absolute path, a path with a `..` segment, a drive or a UNC prefix is reported for
        its form, not only for naming nothing git tracks: each path below would name a tracked
        file of the product were its prefix or its `..` stripped, or resolved against the
        product's root. The remainders themselves pass first, so the error is the prefix's."""
        # invariant: guidelines-check-code-path/1
        line = "- `src/tokens.css`"
        for remainder in ("src/tokens.css", "tests/fixtures.py", "src/components"):
            with self.subTest(remainder=remainder):
                self.assert_clean(self.check(
                    {STYLEGUIDE_FILE: with_line(STYLEGUIDE, 94, line, "- `%s`" % remainder)}, ()))
        paths = ("/src/tokens.css", "/tests/fixtures.py", "/src/components",
                 PRODUCT_ROOT + "/src/tokens.css",
                 "C:/src/tokens.css", r"C:\src\tokens.css", "C:src/tokens.css",
                 "c:/tests/fixtures.py",
                 r"\src\tokens.css", r"\\host\share\src\tokens.css", "//host/share/src/tokens.css",
                 r"\\?\C:\src\tokens.css", "//?/C:/src/tokens.css",
                 "../product/src/tokens.css", "src/components/../tokens.css",
                 "./src/../src/tokens.css", r"src\..\src\tokens.css")
        for path in paths:
            with self.subTest(path=path):
                text = with_line(STYLEGUIDE, 94, line, "- `%s`" % path)
                fragments = () if "\\" in path or PRODUCT_ROOT in path else (path,)
                self.assert_reported(self.check({STYLEGUIDE_FILE: text}, ()), STYLEGUIDE_FILE,
                                     line=94, fragments=fragments)

    def test_a_tracked_file_or_directory_passes(self):
        """The control of the test above: STYLEGUIDE names a tracked file and a directory whose
        files git tracks."""
        # invariant: guidelines-check-code-path/1
        self.assertIn("- `src/tokens.css`\n- `src/components`\n", STYLEGUIDE)
        self.assert_clean(self.check({STYLEGUIDE_FILE: STYLEGUIDE}, ()))


class CodingFixtures(FormCheckTestCase):
    def test_the_valid_coding_fixtures_pass(self):
        """The general file and the file of a kind, as written above, hold no error, alone and
        beside the styleguide and the guidelines with no template: every coding test breaks one
        thing in them. The exemplar's decision wraps its path and its kind over lines, which
        passes, its whitespace collapsed."""
        # invariant: guidelines-check-form/1
        # invariant: guidelines-check-carrier/1
        # invariant: guidelines-check-kind-index/1
        # invariant: guidelines-check-exemplar/1
        # invariant: guidelines-check-example-files/1
        self.assertIn("\n`src/api/orders/route.ts`", EXEMPLAR_DECISION)
        self.assertIn("\n`endpoint`", EXEMPLAR_DECISION)
        every = dict(CODING_FILES, **{STYLEGUIDE_FILE: STYLEGUIDE, TESTING_FILE: TESTING})
        for name, files in (("coding", CODING_FILES), ("every discipline", every)):
            for options in ((), ("--merge-onto", "none")):
                with self.subTest(name, options=options):
                    self.assert_clean(self.check(files, options))


class CodingForm(FormCheckTestCase):
    def test_a_missing_or_misplaced_standing_check_rule_is_reported(self):
        # invariant: guidelines-check-form/1
        cases = (
            ("no Linter", replaced(CODING, LINTER_HEAD + LINTER_CASES, ""), ("Linter",)),
            ("no Formatter", replaced(CODING, FORMATTER, ""), ("Formatter",)),
            ("no Dependency audit", replaced(CODING, AUDIT_HEAD + AUDIT_CASES, ""),
             ("Dependency audit",)),
            ("Formatter before Linter",
             replaced(CODING, LINTER_HEAD + LINTER_CASES + FORMATTER,
                      FORMATTER + LINTER_HEAD + LINTER_CASES), (("Linter", "Formatter"),)),
        )
        for name, text, fragments in cases:
            with self.subTest(name):
                self.assert_reported_anew(self.check(dict(CODING_FILES, **{CODING_FILE: text}),
                                                     ()), CODING_FILE, fragments=fragments)

    def test_a_standing_check_dropped_without_a_departing_decision_is_reported(self):
        # invariant: guidelines-check-form/1
        for body in ("none — the product has no dependencies yet", "none",
                     "none — ABC-18", "the product has no dependencies yet"):
            with self.subTest(body=body):
                text = replaced(CODING, AUDIT_HEAD + AUDIT_CASES,
                                "### Dependency audit\n\n%s\n\n" % body)
                self.assert_reported_anew(self.check(dict(CODING_FILES, **{CODING_FILE: text}),
                                                     ()), CODING_FILE)

    def test_a_standing_check_dropped_by_a_departing_decision_passes(self):
        """The control of the test above: the audit dropped as the template has it (WAY-202)."""
        # invariant: guidelines-check-form/1
        text = replaced(CODING, AUDIT_HEAD + AUDIT_CASES,
                        "### Dependency audit\n\nnone — ABC-18@%s\n\n" % NO_AUDIT_DECISION_FP)
        self.assert_clean(self.check(dict(CODING_FILES, **{CODING_FILE: text}), ()))

    def test_a_general_file_with_no_kinds_of_code_is_reported(self):
        """The general file alone, so that no file of a kind waits for a row of the table; an
        error the general file alone gives with its table counts for nothing."""
        # invariant: guidelines-check-form/1
        text = replaced(CODING, "## Kinds of code\n\n| Kind | File | When to read |\n"
                                "|---|---|---|\n" + KINDS_ROW + "\n\n", "")
        self.assert_reported_anew(self.check({CODING_FILE: text}, ()), CODING_FILE,
                                  baseline={CODING_FILE: CODING}, fragments=("Kinds of code",))

    def test_a_coding_file_whose_name_and_discipline_disagree_is_reported(self):
        """A file of a kind stands in `guidelines/coding-<kind>.md`, `<kind>` an identifier
        (WAY-167). Each misnamed file stands beside a general file whose table names it, the
        `<kind>` its name gives in *Kind*, so that the error asked for is the one of its name."""
        # invariant: guidelines-check-form/1
        for path, kind in (("guidelines/coding-.md", ""), ("guidelines/coding-Endpoint.md",
                                                            "Endpoint"),
                           ("guidelines/coding--x.md", "-x")):
            with self.subTest(path=path):
                general = replaced(CODING, KINDS_ROW, "| %s | `%s` | before adding or changing "
                                                      "an endpoint |" % (kind, path))
                self.assert_reported(
                    self.check({CODING_FILE: general, path: CODING_ENDPOINT}, ()), path,
                    fragments=(("Discipline", "discipline"),))
        for path, text in ((CODING_ENDPOINT_FILE, TESTING), (CODING_FILE, TESTING),
                           (TESTING_FILE, CODING), ("guidelines/coding-web.md", STYLEGUIDE)):
            with self.subTest(path=path, text=text.split("\n")[0]):
                self.assert_reported(self.check({path: text}, ()), path,
                                     fragments=(("Discipline", "discipline"),))


class CodingCarrier(FormCheckTestCase):
    def test_a_coding_rule_naming_no_invariant_is_reported(self):
        """The coding template requires an invariant in every rule (WAY-196). Each rule loses
        its cases with its invariant, so that no case names an invariant the rule does not."""
        # invariant: guidelines-check-carrier/1
        further = rule("Errors are never swallowed", "ABC-10@" + LINT_DECISION_FP, "none",
                       "a caught error is passed on.", "a caught error is dropped.",
                       "Pass on every error you catch.")
        cases = (
            ("a standing check of the general file", CODING_FILE,
             replaced(CODING, LINTER_HEAD + LINTER_CASES, LINTER_HEAD.replace(
                 "lint-clean@" + LINT_FP, "none"))),
            ("a standing check naming a decision only", CODING_FILE,
             replaced(CODING, LINTER_HEAD + LINTER_CASES, LINTER_HEAD.replace(
                 "lint-clean@" + LINT_FP, "ABC-10@" + LINT_DECISION_FP))),
            ("a further rule of the general file", CODING_FILE,
             replaced(CODING, "## Examples\n", further + "## Examples\n")),
            ("a rule of a kind", CODING_ENDPOINT_FILE,
             replaced(CODING_ENDPOINT, VALIDATES_HEAD + VALIDATES_GOOD + VALIDATES_BAD,
                      VALIDATES_HEAD.replace("endpoint-validates@" + VALIDATES_FP, "none"))),
        )
        for name, path, text in cases:
            with self.subTest(name):
                files = dict(CODING_FILES, **{path: text})
                self.assert_reported_anew(self.check(files, ()), path)

    def test_a_coding_rule_naming_no_decision_is_reported(self):
        # invariant: guidelines-check-carrier/1
        cases = (
            (CODING_FILE, replaced(CODING, "- **Decision:** ABC-11@" + FORMAT_DECISION_FP,
                                   "- **Decision:** none")),
            (CODING_ENDPOINT_FILE, replaced(
                CODING_ENDPOINT, "### Input validated with the shared schema\n\n- **Decision:** "
                "ABC-13@" + EXEMPLAR_DECISION_FP, "### Input validated with the shared schema"
                "\n\n- **Decision:** endpoint-validates@" + VALIDATES_FP)),
        )
        for path, text in cases:
            with self.subTest(path):
                self.assert_reported_anew(self.check(dict(CODING_FILES, **{path: text}), ()), path)


class KindIndex(FormCheckTestCase):
    def test_a_kind_file_no_row_names_is_reported(self):
        # invariant: guidelines-check-kind-index/1
        general = replaced(CODING, KINDS_ROW + "\n", "")
        self.assert_reported_anew(
            self.check({CODING_FILE: general, CODING_ENDPOINT_FILE: CODING_ENDPOINT}, ()),
            (CODING_FILE, CODING_ENDPOINT_FILE))

    def test_a_row_naming_no_file_git_tracks_is_reported(self):
        # invariant: guidelines-check-kind-index/1
        row = "| job | `guidelines/coding-job.md` | before adding or changing a job |"
        general = replaced(CODING, KINDS_ROW + "\n", KINDS_ROW + "\n" + row + "\n")
        for untracked in (None, {"guidelines/coding-job.md": CODING_ENDPOINT.replace(
                "# Coding guidelines — endpoint", "# Coding guidelines — job")}):
            with self.subTest(untracked=bool(untracked)):
                self.assert_reported_anew(
                    self.check({CODING_FILE: general, CODING_ENDPOINT_FILE: CODING_ENDPOINT}, (),
                               untracked=untracked),
                    CODING_FILE, line=line_of(general, row))

    def test_a_row_whose_kind_is_not_its_files_kind_is_reported(self):
        # invariant: guidelines-check-kind-index/1
        for kind in ("handler", "endpoints", "Endpoint", ""):
            with self.subTest(kind=kind):
                row = KINDS_ROW.replace("| endpoint |", "| %s |" % kind if kind else "|  |")
                general = replaced(CODING, KINDS_ROW, row)
                self.assert_reported_anew(
                    self.check({CODING_FILE: general, CODING_ENDPOINT_FILE: CODING_ENDPOINT}, ()),
                    CODING_FILE, line=line_of(general, row))

    def test_a_row_whose_when_to_read_is_empty_is_reported(self):
        # invariant: guidelines-check-kind-index/1
        for cell in ("|  |", "| |"):
            with self.subTest(cell=cell):
                row = "| endpoint | `guidelines/coding-endpoint.md` %s" % cell
                general = replaced(CODING, KINDS_ROW, row)
                self.assert_reported_anew(
                    self.check({CODING_FILE: general, CODING_ENDPOINT_FILE: CODING_ENDPOINT}, ()),
                    CODING_FILE, line=line_of(general, row))

    def test_a_kind_file_with_no_general_file_is_reported(self):
        """Git tracks the file of a kind and no `guidelines/coding.md`: alone, beside guidelines
        of other disciplines, and with the general file standing untracked."""
        # invariant: guidelines-check-kind-index/1
        cases = (
            ("alone", {CODING_ENDPOINT_FILE: CODING_ENDPOINT}, None),
            ("beside other disciplines", {CODING_ENDPOINT_FILE: CODING_ENDPOINT,
                                          STYLEGUIDE_FILE: STYLEGUIDE, TESTING_FILE: TESTING},
             None),
            ("the general file untracked", {CODING_ENDPOINT_FILE: CODING_ENDPOINT},
             {CODING_FILE: CODING}),
        )
        for name, files, untracked in cases:
            with self.subTest(name):
                self.assert_reported_anew(self.check(files, (), untracked=untracked),
                                     (CODING_ENDPOINT_FILE, CODING_FILE, "guidelines"))

    def test_a_row_naming_a_tracked_file_of_no_kind_is_reported(self):
        """A row whose *File* names a file git tracks that is no file `guidelines/coding-<kind>.md`
        — another discipline's guidelines, the general file itself, a file of the code — names a
        file with no `<kind>`, so its *Kind* is not that file's `<kind>`, whatever it reads."""
        # invariant: guidelines-check-kind-index/1
        cases = (
            ("testing", "guidelines/testing.md"),
            ("styleguide", "guidelines/styleguide-web.md"),
            ("coding", "guidelines/coding.md"),
            ("endpoint", "src/api/orders/route.ts"),
        )
        for kind, path in cases:
            with self.subTest(path=path):
                row = "| %s | `%s` | before writing code of that kind |" % (kind, path)
                general = replaced(CODING, KINDS_ROW + "\n", KINDS_ROW + "\n" + row + "\n")
                files = {CODING_FILE: general, CODING_ENDPOINT_FILE: CODING_ENDPOINT,
                         TESTING_FILE: TESTING, STYLEGUIDE_FILE: STYLEGUIDE}
                self.assert_reported_anew(self.check(files, ()), CODING_FILE,
                                          line=line_of(general, row))

    def test_a_kind_file_git_does_not_track_is_no_error(self):
        """The control of the tests above: a file of a kind standing in the working tree but not
        tracked by git is no file of the sentence, so no row is asked to name it and no general
        file is asked to stand beside it."""
        # invariant: guidelines-check-kind-index/1
        general = replaced(CODING, KINDS_ROW + "\n", "")
        cases = (
            ("no row names it", {CODING_FILE: general}),
            ("no general file", {TESTING_FILE: TESTING}),
        )
        for name, files in cases:
            for options in ((), ("--merge-onto", "none")):
                with self.subTest(name, options=options):
                    self.assert_clean(self.check(
                        files, options, untracked={CODING_ENDPOINT_FILE: CODING_ENDPOINT}))


class Exemplar(FormCheckTestCase):
    def check_kind(self, text, untracked=None):
        """Runs the checks of form on the general file and on the file of a kind reading
        `text`."""
        return self.check({CODING_FILE: CODING, CODING_ENDPOINT_FILE: text}, (),
                          untracked=untracked)

    def test_a_kind_file_with_no_exemplar_row_or_more_than_one_is_reported(self):
        # invariant: guidelines-check-exemplar/1
        demoted = "| `src/api/orders/route.ts` | copy | — |"
        both = "ABC-16@" + TWO_EXEMPLARS_DECISION_FP
        cases = (
            ("no exemplar row", replaced(CODING_ENDPOINT, EXEMPLAR_ROW, demoted)),
            ("no row at all", replaced(CODING_ENDPOINT, "%s\n%s\n%s\n" % (
                EXEMPLAR_ROW, COPY_ROW, DO_NOT_COPY_ROW), "")),
            # Both rows name a decision whose binding sentence names both paths and the kind, so
            # that only their number is wrong.
            ("two exemplar rows", replaced(replaced(
                CODING_ENDPOINT, EXEMPLAR_ROW, EXEMPLAR_ROW.replace(
                    "ABC-13@" + EXEMPLAR_DECISION_FP, both)),
                COPY_ROW, "| `src/api/users/route.ts` | exemplar | %s |" % both)),
        )
        for name, text in cases:
            with self.subTest(name):
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_row_whose_status_is_off_the_list_is_reported(self):
        # invariant: guidelines-check-exemplar/1
        for status in ("copied", "do-not-copy", "", "example"):
            with self.subTest(status=status):
                row = COPY_ROW.replace("| copy |", "| %s |" % status if status else "|  |")
                text = replaced(CODING_ENDPOINT, COPY_ROW, row)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE,
                                     line=line_of(text, row))

    def test_a_row_whose_file_is_out_of_the_repository_or_untracked_is_reported(self):
        """Paths of a row that is not the exemplar's, so that no decision is asked to name
        them; each but the last two would name a tracked file were its prefix or `..` stripped."""
        # invariant: guidelines-check-exemplar/1
        paths = ("/src/api/users/route.ts", PRODUCT_ROOT + "/src/api/users/route.ts",
                 "../product/src/api/users/route.ts", "src/api/../api/users/route.ts",
                 "C:/src/api/users/route.ts", r"C:\src\api\users\route.ts",
                 r"\\host\share\src\api\users\route.ts", "//host/share/src/api/users/route.ts",
                 "src/api/missing/route.ts", "src/api/draft/route.ts")
        for path in paths:
            with self.subTest(path=path):
                row = COPY_ROW.replace("`src/api/users/route.ts`", "`%s`" % path)
                text = replaced(CODING_ENDPOINT, COPY_ROW, row)
                self.assert_reported_anew(
                    self.check_kind(text, untracked={"src/api/draft/route.ts": "export {};\n"}),
                    CODING_ENDPOINT_FILE, line=line_of(text, row))

    def test_a_row_other_than_the_exemplar_naming_a_decision_is_reported(self):
        # invariant: guidelines-check-exemplar/1
        for value in ("ABC-13@" + EXEMPLAR_DECISION_FP, "none", ""):
            with self.subTest(value=value):
                row = COPY_ROW.replace("| — |", "| %s |" % value if value else "|  |")
                text = replaced(CODING_ENDPOINT, COPY_ROW, row)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE,
                                     line=line_of(text, row))

    def test_an_exemplar_row_whose_decision_does_not_designate_it_is_reported(self):
        """The exemplar's *Decision* names a decision the log does not hold, one it repealed,
        none, or one whose binding sentences lack the row's *File* in backticks or the kind
        `endpoint` in backticks."""
        # invariant: guidelines-check-exemplar/1
        cases = (
            ("a decision the log does not hold", "ABC-09@0123abcd"),
            ("a repealed decision", "ABC-04@" + FONT_FP),
            ("no decision", "—"),
            ("the kind alone", "ABC-14@" + KIND_ONLY_DECISION_FP),
            ("the path with the kind bare", "ABC-15@" + PATH_ONLY_DECISION_FP),
            ("the path bare with the kind", "ABC-17@" + BARE_PATH_DECISION_FP),
            ("neither path nor kind", "ABC-10@" + LINT_DECISION_FP),
        )
        for name, value in cases:
            with self.subTest(name):
                row = EXEMPLAR_ROW.replace("ABC-13@" + EXEMPLAR_DECISION_FP, value)
                text = replaced(CODING_ENDPOINT, EXEMPLAR_ROW, row)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE,
                                     line=line_of(text, row))


class ExampleFiles(FormCheckTestCase):
    def check_kind(self, text):
        return self.check({CODING_FILE: CODING, CODING_ENDPOINT_FILE: text}, ())

    def test_a_rule_naming_an_invariant_without_its_good_or_bad_case_is_reported(self):
        """Every discipline: a coding rule of a kind and of the general file, a styleguide's rule,
        and a rule of guidelines with no template once it names an invariant (WAY-168)."""
        # invariant: guidelines-check-example-files/1
        testing_named = replaced(TESTING, "- **Invariant:** none",
                                 "- **Invariant:** lint-clean@" + LINT_FP)
        cases = (
            ("no good case", CODING_ENDPOINT_FILE, replaced(CODING_ENDPOINT, VALIDATES_GOOD, "")),
            ("no bad case", CODING_ENDPOINT_FILE, replaced(CODING_ENDPOINT, VALIDATES_BAD, "")),
            ("no case", CODING_ENDPOINT_FILE,
             replaced(CODING_ENDPOINT, VALIDATES_GOOD + VALIDATES_BAD, "")),
            ("a standing check with no case", CODING_FILE, replaced(CODING, LINTER_CASES, "")),
            ("a styleguide's rule with no case", STYLEGUIDE_FILE,
             replaced(STYLEGUIDE, EACH_ROLE_CASES, "")),
            ("a rule with no template naming an invariant", TESTING_FILE, testing_named),
        )
        for name, path, text in cases:
            with self.subTest(name):
                files = dict(CODING_FILES, **{path: text})
                self.assert_reported_anew(self.check(files, ()), path)

    def test_a_rule_naming_two_invariants_without_the_cases_of_one_is_reported(self):
        # invariant: guidelines-check-example-files/1
        handler_good, handler_bad = (HANDLER_CASES[:HANDLER_CASES.index("```bad")],
                                     HANDLER_CASES[HANDLER_CASES.index("```bad"):])
        cases = (
            ("no case of the second", replaced(CODING_ENDPOINT, LOCATION_CASES, "")),
            ("no case of the first", replaced(CODING_ENDPOINT, HANDLER_CASES, "")),
            ("no bad case of the first", replaced(CODING_ENDPOINT, handler_bad, "")),
            ("no good case of the first", replaced(CODING_ENDPOINT, handler_good, "")),
        )
        for name, text in cases:
            with self.subTest(name):
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_second_case_of_one_kind_for_an_invariant_is_reported(self):
        # invariant: guidelines-check-example-files/1
        second_good = VALIDATES_GOOD.replace("src/api/carts/route.ts", "src/api/baskets/route.ts")
        second_bad = VALIDATES_BAD.replace("src/api/carts/route.ts", "src/api/baskets/route.ts")
        for name, old, new in (("two good cases", VALIDATES_GOOD, VALIDATES_GOOD + second_good),
                               ("two bad cases", VALIDATES_BAD, VALIDATES_BAD + second_bad)):
            with self.subTest(name):
                self.assert_reported_anew(self.check_kind(replaced(CODING_ENDPOINT, old, new)),
                                     CODING_ENDPOINT_FILE)

    def test_a_case_naming_an_invariant_its_rule_does_not_name_is_reported(self):
        """A pair of cases added for an invariant of the invariants file that the rule's
        *Invariant* does not name: one no rule of the file names, one another rule names, and
        the product's `guidelines-form`."""
        # invariant: guidelines-check-example-files/1
        for identifier in ("lint-clean", "endpoint-handler", "guidelines-form", "missing-check"):
            with self.subTest(identifier=identifier):
                extra = (case("good", identifier, "src/api/carts/route.ts", "export {};")
                         + case("bad", identifier, "src/api/carts/route.ts", "export const x;"))
                text = replaced(CODING_ENDPOINT, VALIDATES_BAD, VALIDATES_BAD + extra)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_case_whose_path_is_out_of_the_repository_is_reported(self):
        """The path of a case may name a file that does not exist, but never one outside the
        product's root: absolute, with a `..` segment, a drive or a UNC prefix."""
        # invariant: guidelines-check-example-files/1
        opening = "```good endpoint-validates src/api/carts/route.ts"
        for path in ("/src/api/carts/route.ts", "../src/api/carts/route.ts",
                     "src/../src/api/carts/route.ts", "src/api/carts/../route.ts",
                     "C:/src/api/carts/route.ts", r"C:\src\api\carts\route.ts",
                     "C:src/api/carts/route.ts", r"\\host\share\route.ts", "//host/share/route.ts"):
            with self.subTest(path=path):
                text = replaced(CODING_ENDPOINT, opening, "```good endpoint-validates " + path)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_case_whose_path_names_no_file_yet_passes(self):
        """The control of the test above: the fixture's cases stand at paths no file holds, as
        `src/api/carts/route.ts`, which is no error (WAY-168: added at that path)."""
        # invariant: guidelines-check-example-files/1
        self.assertNotIn("src/api/carts/route.ts", FOUNDATION)
        self.assertIn("```good endpoint-validates src/api/carts/route.ts\n", CODING_ENDPOINT)
        self.assert_clean(self.check(CODING_FILES, ()))

    def test_a_line_that_would_open_a_fence_inside_a_case_is_reported(self):
        """A line of three backticks or tildes after at most three spaces, with or without an
        info string, inside a case. A bare line of three backticks closes the case there, and
        the case's own closing line then opens a block that is no case."""
        # invariant: guidelines-check-example-files/1
        inside = "export const POST = handle((input: unknown) => input);\n```"
        for fence in ("~~~", "~~~ts", "```ts", "   ```ts", "  ~~~", "````", "```"):
            with self.subTest(fence=fence):
                new = "export const POST = handle((input: unknown) => input);\n%s\n```" % fence
                text = replaced(CODING_ENDPOINT, VALIDATES_BAD,
                                replaced(VALIDATES_BAD, inside, new))
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_case_left_open_to_the_end_of_the_file_is_reported(self):
        """The last case of the file loses its closing line, so that no later fence closes it and
        no line inside it would open one. It swallows the sections after it, whose absence the
        form check reports apart; the error asked for is the one at the case's opening line."""
        # invariant: guidelines-check-example-files/1
        location_bad = LOCATION_CASES[LOCATION_CASES.index("```bad"):]
        background_bad = BACKGROUND_CASES[BACKGROUND_CASES.index("```bad"):]
        cases = (
            ("the last case of a file of a kind", CODING_ENDPOINT_FILE, CODING_ENDPOINT,
             location_bad, "```bad endpoint-location src/carts/route.ts"),
            ("the last case of a styleguide", STYLEGUIDE_FILE, STYLEGUIDE, background_bad,
             "```bad background-pair src/tokens.css"),
        )
        for name, path, valid, last, opening in cases:
            with self.subTest(name):
                self.assertTrue(last.endswith("\n```\n\n"))
                self.assertNotIn("```", valid[valid.index(last) + len(last):])
                text = replaced(valid, last, last[:-len("```\n\n")])
                files = dict(CODING_FILES, **{path: text})
                self.assert_reported_anew(self.check(files, ()), path,
                                          line=line_of(text, opening),
                                          fragments=("end of the file",))

    def test_another_fenced_block_in_a_rule_carrying_cases_is_reported(self):
        """In a rule whose cases are required, every fenced block is a case: a block with
        another info string, with none, or a case's info string lacking its path."""
        # invariant: guidelines-check-example-files/1
        blocks = ("```ts\nconst limit = 10;\n```\n\n", "```\nconst limit = 10;\n```\n\n",
                  "```sample endpoint-validates src/api/carts/route.ts\nexport {};\n```\n\n",
                  "```good endpoint-validates\nexport {};\n```\n\n",
                  "~~~ts\nconst limit = 10;\n~~~\n\n")
        for block in blocks:
            with self.subTest(block=block.split("\n")[0]):
                text = replaced(CODING_ENDPOINT, VALIDATES_BAD, VALIDATES_BAD + block)
                self.assert_reported_anew(self.check_kind(text), CODING_ENDPOINT_FILE)

    def test_a_rule_naming_only_guidelines_form_needs_no_cases(self):
        """The exemption: a rule whose *Invariant* is the product's `guidelines-form` gives no
        case, and a rule naming it beside another invariant gives the cases of the other alone
        (WAY-168)."""
        # invariant: guidelines-check-example-files/1
        alone = replaced(with_line(STYLEGUIDE, 40, "- **Invariant:** background-pair@" + PAIR_FP,
                                   "- **Invariant:** guidelines-form@" + GUIDELINES_FORM_FP),
                         BACKGROUND_CASES, "")
        beside = with_line(STYLEGUIDE, 40, "- **Invariant:** background-pair@" + PAIR_FP,
                           "- **Invariant:** guidelines-form@%s · background-pair@%s"
                           % (GUIDELINES_FORM_FP, PAIR_FP))
        for name, text in (("guidelines-form alone", alone), ("beside another", beside)):
            with self.subTest(name):
                self.assert_clean(self.check({STYLEGUIDE_FILE: text}, ()))

    def test_a_rule_naming_guidelines_form_beside_another_without_the_others_cases_is_reported(
            self):
        """The exemption reaches `guidelines-form` alone: a rule whose *Invariant* names it beside
        another invariant still gives, for that other, exactly one good and one bad case, wherever
        `guidelines-form` stands in the field."""
        # invariant: guidelines-check-example-files/1
        pair_good = BACKGROUND_CASES[:BACKGROUND_CASES.index("```bad")]
        pair_bad = BACKGROUND_CASES[BACKGROUND_CASES.index("```bad"):]
        styleguide = with_line(STYLEGUIDE, 40, "- **Invariant:** background-pair@" + PAIR_FP,
                               "- **Invariant:** guidelines-form@%s · background-pair@%s"
                               % (GUIDELINES_FORM_FP, PAIR_FP))
        styleguide_after = with_line(STYLEGUIDE, 40, "- **Invariant:** background-pair@" + PAIR_FP,
                                     "- **Invariant:** background-pair@%s · guidelines-form@%s"
                                     % (PAIR_FP, GUIDELINES_FORM_FP))
        endpoint = replaced(CODING_ENDPOINT, "- **Invariant:** endpoint-validates@" + VALIDATES_FP,
                            "- **Invariant:** guidelines-form@%s · endpoint-validates@%s"
                            % (GUIDELINES_FORM_FP, VALIDATES_FP))
        cases = (
            ("a styleguide's rule with no case of the other", STYLEGUIDE_FILE,
             replaced(styleguide, BACKGROUND_CASES, "")),
            ("a styleguide's rule with no good case of the other", STYLEGUIDE_FILE,
             replaced(styleguide, pair_good, "")),
            ("a styleguide's rule with no bad case of the other", STYLEGUIDE_FILE,
             replaced(styleguide, pair_bad, "")),
            ("guidelines-form named second, no case of the other", STYLEGUIDE_FILE,
             replaced(styleguide_after, BACKGROUND_CASES, "")),
            ("a coding rule with no case of the other", CODING_ENDPOINT_FILE,
             replaced(endpoint, VALIDATES_GOOD + VALIDATES_BAD, "")),
        )
        for name, path, text in cases:
            with self.subTest(name):
                files = dict(CODING_FILES, **{path: text})
                self.assert_reported_anew(self.check(files, ()), path)


if __name__ == "__main__":
    unittest.main()
