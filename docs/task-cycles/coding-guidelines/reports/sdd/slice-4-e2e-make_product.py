"""Writes a temporary product for the end-to-end check of Slice 4: a part map, a decision log
(one decision designating the exemplar by path and kind), an invariants file, coding guidelines
filled from the coding template with a pair of cases per named invariant, and a root AGENTS.md
naming `guidelines/coding.md`. Usage: python3 -B make_product.py <the-way> <product-dir>"""

import importlib.util
import os
import subprocess
import sys

THE_WAY, ROOT = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location(
    "fp", os.path.join(THE_WAY, "relation-model", "fingerprint.py"))
fp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fp)

PART_MAP = """# Part map

## web — The web interface and its API

The part answers for the product's code.

- **Files:** src/**
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

## build — The build configuration

The part answers for the build configuration, the tools' configuration and the lockfile.

- **Files:** package.json
  package-lock.json
  eslint.config.js
  .prettierrc
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

## agent-instructions — What directs whoever carries out the product's tasks

The part answers for the instruction files and the guidelines.

- **Files:** AGENTS.md
  guidelines/**
  tests/**
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none

## foundation — The product's foundation

- **Files:** foundations/**
- **Depends on:** none
- **Failure modes:** none
- **Trust boundary:** none
"""

DECISIONS = [
    (1, "Which linter reads the product's code?",
     "Every file of the product's code passes the linter ESLint with the product's configuration, "
     "the rules no-unused-vars and eqeqeq blocking."),
    (2, "Which formatter writes the product's code?",
     "Every file of the product's code stands as the formatter Prettier writes it."),
    (3, "How are the product's dependencies audited?",
     "No change brings in a dependency version with a known vulnerability of high severity or "
     "above, as npm audit reports it from its live advisory database."),
    (4, "Which file is the exemplar of an endpoint?",
     "The file `src/api/orders/route.ts` is the exemplar of the kind `endpoint`: every endpoint "
     "validates its input with the shared schema and answers through the shared handler."),
]


def decision(number, question, binding):
    return "\n".join([
        "### ABC-%02d/1 — %s" % (number, question), "", binding, "",
        "- **Change:** new decision", "- **Scope:** web", "- **Based on:** none",
        "- **Relations:** none",
        "- **Verification:** level 1 — a script checks it",
        "- **Review when:** none", "- **Origin:** none",
        "- **Approved by:** Anna, 2026-10-19", "",
        "*Rationale:* one way for the whole code.", "*Rejected:* none considered"])


LOG = ("# Decision log\n\nThe product's decisions.\n\n"
       + "\n\n".join(decision(*each) for each in DECISIONS) + "\n")
DFP = {number: fp.fingerprint(binding) for number, _, binding in DECISIONS}

INVARIANTS = [
    ("lint-clean", "No file of the parts web and build breaks a rule of ESLint that blocks.", 1),
    ("format-clean", "Every file of the parts web and build stands as Prettier leaves it.", 2),
    ("audit-clean", "The change against {fork-point} brings in no dependency version with a known "
                    "vulnerability of high severity or above.", 3),
    ("endpoint-validates", "Every file of the kind endpoint validates its input with the shared "
                           "schema.", 4),
    ("endpoint-handler", "Every file of the kind endpoint answers through the shared handler.", 4),
]
GUIDELINES_FORM = (
    "Every file `guidelines/<name>.md` holds, in their order, the header lines, sections, rules, "
    "rule fields and tables that the template of guidelines and the template of its discipline "
    "require at the commit of the-way the repository uses — the commit checked, in the-way itself, "
    "and the pinned commit, in a product — each with the values and the links those templates give "
    "it, with a name that agrees with its *Discipline*, each section or rule it drops reading "
    "`none —` with a decision of the log and that decision's fingerprint, each part it names being "
    "a part of the map, and each path under `## Where in code` naming something git tracks.")


def entry(identifier, sentence, derives):
    return "\n".join([
        "## %s/1" % identifier, "", sentence, "",
        "- **Method:** `node tests/check_%s.js`" % identifier.replace("-", "_"),
        "- **Rests on:** none", "- **Derives from:** %s" % derives, "- **Part:** web · build",
        "- **Correction:** none"])


INVARIANTS_FILE = ("# Invariants\n\n"
                   + "\n\n".join([entry(i, s, "ABC-%02d@%s" % (d, DFP[d]))
                                  for i, s, d in INVARIANTS]
                                 + [entry("guidelines-form", GUIDELINES_FORM, "none")])
                   + "\n\n## Withdrawn identifiers\n\n| Identifier | Why | Successors |\n"
                     "|---|---|---|\n\n## Quarantined invariants\n\n"
                     "| Identifier | Version | Until |\n|---|---|---|\n")
IFP = {i: fp.fingerprint(s) for i, s, _ in INVARIANTS}
IFP["guidelines-form"] = fp.fingerprint(GUIDELINES_FORM)


def ref_d(number):
    return "ABC-%02d@%s" % (number, DFP[number])


def ref_i(identifier):
    return "%s@%s" % (identifier, IFP[identifier])


def case(which, identifier, path, *lines):
    return "```%s %s %s\n%s\n```\n" % (which, identifier, path, "\n".join(lines))


CODING = f"""# Coding guidelines — the shop

- **Discipline:** coding
- **Applies to:** web · build

## When to read

Before any change of the product's code.

## Kinds of code

| Kind | File | When to read |
|---|---|---|
| endpoint | `guidelines/coding-endpoint.md` | before adding or changing an endpoint |

## Rules

### Linter

- **Decision:** {ref_d(1)}
- **Invariant:** {ref_i("lint-clean")}
- **Good:** a function reads every variable it declares.
- **Bad:** a function declares a variable it never reads.

Run ESLint with the product's configuration; fix a report of a rule that blocks in the file
that gives it, with no inline suppression.

{case("good", "lint-clean", "src/lib/sum.ts", "export const sum = (a: number, b: number) => a + b;")}
{case("bad", "lint-clean", "src/lib/sum.ts", "export const sum = (a: number, b: number) => {", "  const unused = 1;", "  return a + b;", "};")}
### Formatter

- **Decision:** {ref_d(2)}
- **Invariant:** {ref_i("format-clean")}
- **Good:** a file stands as Prettier writes it.
- **Bad:** a file keeps spacing Prettier would change.

Let Prettier write every file of the code before the change is offered.

{case("good", "format-clean", "src/lib/sum.ts", "export const sum = (a: number, b: number) => a + b;")}
{case("bad", "format-clean", "src/lib/sum.ts", "export const sum=(a:number,b:number)=>a+b")}
### Dependency audit

- **Decision:** {ref_d(3)}
- **Invariant:** {ref_i("audit-clean")}
- **Good:** the change brings in a version npm audit flags nothing in.
- **Bad:** the change brings in a version with a known vulnerability of high severity.

Run npm audit on the change before taking in a dependency.

{case("good", "audit-clean", "tools/one/package-lock.json", '{{"lockfileVersion": 3, "packages": {{"node_modules/left-pad": {{"version": "1.3.0"}}}}}}')}
{case("bad", "audit-clean", "tools/one/package-lock.json", '{{"lockfileVersion": 3, "packages": {{"node_modules/minimist": {{"version": "0.0.8"}}}}}}')}
## Examples

### Short functions

The team keeps a function short enough to read at a glance.

## Where in code

- `eslint.config.js`
- `.prettierrc`
- `package.json`
- `src`
"""

CODING_ENDPOINT = f"""# Coding guidelines — endpoint

- **Discipline:** coding
- **Applies to:** web

## When to read

Before adding or changing a file of the kind endpoint.

## Files of this kind

| File | Status | Decision |
|---|---|---|
| `src/api/orders/route.ts` | exemplar | {ref_d(4)} |
| `src/api/users/route.ts` | copy | — |
| `src/api/legacy/route.ts` | do not copy | — |

## Rules

### Input validated with the shared schema

- **Decision:** {ref_d(4)}
- **Invariant:** {ref_i("endpoint-validates")}
- **Good:** an endpoint parses its input with the shared schema.
- **Bad:** an endpoint reads its input unchecked.

Parse the input with the shared schema before reading it.

{case("good", "endpoint-validates", "src/api/carts/route.ts", 'import { handle } from "../handler";', 'import { schema } from "../schema";', "export const POST = handle((input: unknown) => schema.parse(input));")}
{case("bad", "endpoint-validates", "src/api/carts/route.ts", 'import { handle } from "../handler";', "export const POST = handle((input: unknown) => input);")}
### Through the shared handler

- **Decision:** {ref_d(4)}
- **Invariant:** {ref_i("endpoint-handler")} · {ref_i("guidelines-form")}
- **Good:** an endpoint answers through the shared handler.
- **Bad:** an endpoint answers on its own.

Answer every request through the shared handler.

{case("good", "endpoint-handler", "src/api/carts/route.ts", 'import { handle } from "../handler";', "export const POST = handle((input: unknown) => input);")}
{case("bad", "endpoint-handler", "src/api/carts/route.ts", "export const POST = (input: unknown) => new Response(String(input));")}
## Examples

### Names of inputs

The exemplar names each input after what it holds.

## Where in code

- `src/api`
"""

AGENTS = """# Working in the shop

Before any change of the product's code, read `guidelines/coding.md`; it names the file of each
kind of code and when to read it.

Run the tests with `npm test` before offering a change.
"""

FILES = {
    "foundations/part_map.md": PART_MAP,
    "foundations/decisions.md": LOG,
    "foundations/invariants.md": INVARIANTS_FILE,
    "guidelines/coding.md": CODING,
    "guidelines/coding-endpoint.md": CODING_ENDPOINT,
    "AGENTS.md": AGENTS,
    "package.json": '{"name": "shop", "scripts": {"test": "node --test"}}\n',
    "package-lock.json": '{"lockfileVersion": 3}\n',
    "eslint.config.js": "export default [];\n",
    ".prettierrc": "{}\n",
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

os.makedirs(ROOT)
for path, text in FILES.items():
    full = os.path.join(ROOT, *path.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
git = ["git", "-c", "user.name=Gate", "-c", "user.email=gate@example.com", "-c",
       "core.autocrlf=false"]
subprocess.run(git + ["init", "-q", "-b", "main"], cwd=ROOT, check=True)
subprocess.run(git + ["add", "-A"], cwd=ROOT, check=True)
subprocess.run(git + ["commit", "-q", "-m", "product"], cwd=ROOT, check=True)
print("written:", ROOT)
